-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: sys
-- ------------------------------------------------------
-- Server version	5.7.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `events`
--

DROP TABLE IF EXISTS `events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `events` (
  `event_id` char(10) NOT NULL,
  `event_title` varchar(100) DEFAULT NULL,
  `link` char(100) DEFAULT NULL,
  `id` int(11) DEFAULT NULL,
  `title` varchar(20) DEFAULT NULL,
  `date` char(20) DEFAULT NULL,
  `type` varchar(45) DEFAULT NULL,
  `coordinates` char(200) DEFAULT NULL,
  PRIMARY KEY (`event_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events`
--

LOCK TABLES `events` WRITE;
/*!40000 ALTER TABLE `events` DISABLE KEYS */;
INSERT INTO `events` VALUES ('EONET_3460','Volgogradskaya Oblast, Russia Flooding','https://eonet.sci.gsfc.nasa.gov/api/v2.1/events/EONET_3460',9,'Floods','2018-04-04T00:00:00Z','Point','[43.4306, 50.319]'),('EONET_3461','Thrace, Greece Floods','https://eonet.sci.gsfc.nasa.gov/api/v2.1/events/EONET_3461',9,'Floods','2018-03-27T00:00:00Z','Point','[26.5, 41.25]'),('EONET_3465','Ebro River, Spain Flood','https://eonet.sci.gsfc.nasa.gov/api/v2.1/events/EONET_3465',9,'Floods','2018-04-12T00:00:00Z','Polygon','[[[-2.84912109375, 41.37201604041778], [-2.84912109375, 42.96219666198758], [-0.44921875, 42.96219666198758], [-0.44921875, 41.37201604041778], [-2.84912109375, 41.37201604041778]]]'),('EONET_3468','Avian Complex Fire','https://eonet.sci.gsfc.nasa.gov/api/v2.1/events/EONET_3468',8,'Wildfires','2018-04-16T15:45:00Z','Point','[-80.902, 26.01]'),('EONET_3469','34 Complex Fire','https://eonet.sci.gsfc.nasa.gov/api/v2.1/events/EONET_3469',8,'Wildfires','2018-04-12T16:00:00Z','Point','[-99.4, 36.52]'),('EONET_3470','Rhea Fire','https://eonet.sci.gsfc.nasa.gov/api/v2.1/events/EONET_3470',8,'Wildfires','2018-04-12T14:00:00Z','Point','[-99.213, 35.849]'),('EONET_3471','Diener Canyon Fire','https://eonet.sci.gsfc.nasa.gov/api/v2.1/events/EONET_3471',8,'Wildfires','2018-04-12T16:00:00Z','Point','[-108.136, 35.191]'),('EONET_3472','Bluewater Fire','https://eonet.sci.gsfc.nasa.gov/api/v2.1/events/EONET_3472',8,'Wildfires','2018-04-12T12:00:00Z','Point','[-108.133, 35.25]'),('EONET_3473','Rattlesnake Fire','https://eonet.sci.gsfc.nasa.gov/api/v2.1/events/EONET_3473',8,'Wildfires','2018-04-11T13:30:00Z','Point','[-109.506, 33.656]'),('EONET_3474','Mile Marker 117 Fire','https://eonet.sci.gsfc.nasa.gov/api/v2.1/events/EONET_3474',8,'Wildfires','2018-04-17T00:00:00Z','Point','[-104.673, 38.528]'),('EONET_3477','Kauai, Hawaii Flooding','https://eonet.sci.gsfc.nasa.gov/api/v2.1/events/EONET_3477',9,'Floods','2018-04-14T00:00:00Z','Point','[-159.5, 22.02]'),('EONET_3478','Moffat Fire, California','https://eonet.sci.gsfc.nasa.gov/api/v2.1/events/EONET_3478',8,'Wildfires','2018-04-19T10:28:00Z','Point','[-118.08449, 36.71537]');
/*!40000 ALTER TABLE `events` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-04-23  2:39:43
