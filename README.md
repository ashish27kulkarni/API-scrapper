# API-scrapper
Scrapper to fetch data from API and push into database.
Priliminary instructions for running the project file (project.py)

1) The Python Version used is Python 3.6. Code might be unstable is any other Python version is used.
2) Before running the code, a few packages have to be installed on the system running the code. 
	1) requests (pip install requests)
	2) json
	3) mysql.connector (pip install mysql-connector)
3) The Database used is in MySQL, with local connection.
4) To read the code, the .py file can be opened in IDLE (3.6) or I personally use text editors like nano or vim in Windows Powershell/Terminal.
5) To run the code, open Powershell/cmd in Windows or Terminal in Linux, and run the following command,
	$Python pp1.py
   Before any initialization, the program will ask for the Database password, for security reasons, once granted, the program will run.
   NOTE: Current database password is empty, so please press ENTER when prompted for access.
         When importing the .sql file to a new database, please enter the new database login details in the program for access.
   This will start the program, and initialize the connections to the API and the Database.
   The program will now ask weather the user would to send an e-mail containing the output CSV file to intended e-mail address?
   The program will accept only YES ("Y" or "y") OR, NO ("N" or "n")
   	If answered with a "Y" or "y", the program will ask for your e-address. Enter your Gmail address.
   	The program will then ask for Password, even when you type the password, no value will be displayed on the command prompt, press enter after entering password.
   	Enter the e-mail address who will the e-mail containing the CSV file. 
   	NOTE: G-Mail does not allow unsecure apps direct access. 
         	This has to be changed by going on the browser, to ("https://myaccount.google.com/lesssecureapps"), and turning the Option for 
	 	"ALLOW LESS SECURE APPS: " to "ON".
		IF THIS STEP IS NOT FOLLOWED, THE SERVER WILL NOT AUTHENTICATE THE USER, RESULTING IN FAILURE OF SENDING OF E-MAIL.
   	Once this data is entered, the program will fetch data from the API, parse it, push it into the CSV as well as the MySQL Database.
	
	If answered with a "N" or "n", the program will fetch the data from the API, and push it into the CSV and Database, no further input will be necessary.

   A successful write operation to the CSV and Database will be displayed.


 

