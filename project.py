import requests
import json
import re
import collections
from collections import OrderedDict
import mysql.connector
import csv
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import getpass


class Scrapper:
        def __init__(self, url, dbUser, dbTable, dbPassword, dbHost, dbDatabase):               #Initialize connections to the URL and Database
                self.url = url
                self.dbUser = dbUser
                self.dbTable = dbTable
                self.dbPassword = dbPassword
                self.dbHost = dbHost
                self.dbDatabase = dbDatabase
                self.response = requests.get(self.url)
                self.data = self.response.text
                self.parsed = json.loads(self.data)                                             #Buffered JSON data
                #ENTER/CHANGE THE DATABASE USERNAME AND HOST HERE  
                self.connection = mysql.connector.connect(user = self.dbUser, password = self.dbPassword, host = dbHost)
                self.cursor = self.connection.cursor()                                          #Initialize CURSOR for Database operations with Python
                #print(self.parsed)

        def result_set(self):
                with open('project_Output.csv', 'w', newline = '') as out:                      #Open intended CSV file
                        csv_out = csv.writer(out)
                        csv_out.writerow(['Event ID', 'Event title', 'Link', 'ID', 'Title', 'Date', 'Type', 'Cooridnates']) #Headers for CSV file
                        print("CSV File loaded.......................")                         
                        for each in self.parsed['events']:                                      #Enter the heavily nested JSON data
                                self.event_id = each['id']                              
                                self.event_title = each['title']
                                self.link = each['link']
                                self.categories = each['categories']
                                self.geometries = each['geometries']
                                for each in self.categories:                                    #Accessing 3rd degree of iterations
                                        self.id = each['id']                                    #PRIMARY KEY
                                        self.title = each['title']
                                        continue
                                for each in self.geometries:                                    #Accessing 3rd degree of iterations
                                        self.date = each['date']
                                        self.type = each['type']
                                        self.coordinates = each['coordinates']
                                        self.coordinates = str(self.coordinates)                #Convert for ease of database operations
                                        #self.coordinates = ("'" + self.coordinates + "'")
                                        continue
                                if (self.date >= "2018-03"):                                    #Finding events from March and April 2018
                                        if (self.title == "Wildfires" or self.title == "Landslides" or self.title == "Storms" or self.title == "Floods"):
                                                dictEventFields = (self.event_id, self.event_title, self.link, self.id, self.title, self.date, self.type, self.coordinates)                                                
                                                csv_out.writerow(dictEventFields)               #Writing data to the CSV 
                                                strEventFields = str(dictEventFields)
                                                SQL = ("""                                      
                                                        INSERT INTO """ + self.dbDatabase + "." + self.dbTable +
                                                       """ (`event_id`,
                                                        `event_title`,
                                                        `link`,
                                                        `id`,
                                                        `title`,
                                                        `date`,
                                                        `type`,
                                                        `coordinates`)
                                                        VALUES """ + 
                                                        strEventFields +
                                                       " ; "
                                                        )                                       #Creating dynamic SQL statements to inject directly to Database from Python
                                                #print (SQL)
                                                try:
                                                       self.cursor.execute(SQL)                 #Execute the SQL statement
                                                       self.cursor.fetchwarnings()
                                                       self.connection.commit()                 #Commit the changes to the database before next row is iterated
                                                       rows_affected = self.cursor.rowcount
                                                       if rows_affected == 0:
                                                               print("No Insert")
                                                       else:
                                                               print("Database Updated.........................")
                                                except mysql.connector.Error as err:
                                                       print ("Something went wrong:{}", format(err))                                                                        
                        print ("CSV FIle Ready.........................")

                                        
        def dbClose(self):
                self.cursor.close()
                self.connection.close()                                                         #Close database conenction

        def sendEmail(self, emailFrom, password, emailTo):
                self.emailFrom = emailFrom                                                      #Get user details directly for security purposes
                self.emailTo = emailTo
                self.fileToSend = "project_Output.csv"
                self.username = emailFrom
                self.password = password
                self.msg = MIMEMultipart()
                self.msg["From"] = self.emailFrom
                self.msg["To"] = self.emailTo
                self.msg["Subject"] = "TEXT"
                self.preamble = "TEXT"

                ctype, encoding = mimetypes.guess_type(self.fileToSend)
                if ctype is None or encoding is not None:
                        ctype = "application/octet-stream"

                maintype, subtype = ctype.split("/", 1)
                if maintype == "text":
                        fp = open (self.fileToSend)
                        attachment = MIMEText(fp.read(), _subtype = suntype)
                        fp.close()
                else:
                        fp = open (self.fileToSend, "rb")
                        attachment = MIMEBase(maintype, subtype)
                        attachment.set_payload(fp.read())
                        fp.close()
                        encoders.encode_base64(attachment)

                attachment.add_header("Content-Disposition", "attachment", filename = self.fileToSend)
                self.msg.attach(attachment)                                                     #Attaching the CSV file to the email message

                server = smtplib.SMTP("smtp.gmail.com:587")                                     #Initializing connection to the GMAIL server
                server.starttls()
                server.login(self.username, self.password)                                      #Login GMAIL with user specified details
                print("E-Mail access granted..............")
                server.sendmail(self.emailFrom, self.emailTo, self.msg.as_string())             #E-mail send operation
                print("E-mail sent........................")                                    
                server.quit()

                                        ############# END OF CLASS SCRAPPER #############                


dbUser = input ('Please Enter the Username of Your Database:    ')
dbPassword = getpass.getpass(prompt = 'Please Enter Database Password Before Proceding: ', stream = None)
dbHost = input ('Please Enter Your Host of Database:    ')
dbDatabase = input ('Please Enter the Name of your Database:   ')
dbTable = input ('Please Enter the Name of Your Database Table:    ')
question = input ('Would You Like to Send an E-mail As Well Today? ')                           #Keeping an option to send the E-mail
p = Scrapper("https://eonet.sci.gsfc.nasa.gov/api/v2.1/events", dbUser, dbTable, dbPassword, dbHost, dbDatabase)     #Feeding the URL here, can be made dynamic for code reusability
if (question == "Y" or question == "y"):
        emailFrom = input('Please Enter Your GMail E-Mail Address:  ')
        password = getpass.getpass(prompt = 'Password: ', stream = None)                        #Password protection method
        emailTo = input('Please Enter the E-Maill Address Who Would Recieve E-Mail:   ')
        p.result_set()
        p.dbClose()
        p.sendEmail(emailFrom, password, emailTo)                                               #E-Mail option available only if user wants to

elif (question == "N" or question == "n"):
        p.result_set()
        p.dbClose()

else:
        print("Wrong Input!")
        exit()

        


