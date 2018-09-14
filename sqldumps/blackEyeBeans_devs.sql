-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: blackEyeBeans
-- ------------------------------------------------------
-- Server version	5.7.23-0ubuntu0.18.04.1

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
-- Table structure for table `devs`
--

DROP TABLE IF EXISTS `devs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `devs` (
  `dev_id` int(11) NOT NULL AUTO_INCREMENT,
  `dev_ip` varchar(45) NOT NULL,
  `dev_domains` varchar(255) DEFAULT NULL,
  `dev_state` varchar(45) DEFAULT NULL,
  `dev_ports` varchar(255) DEFAULT NULL,
  `dev_portsstate` varchar(255) DEFAULT NULL,
  `dev_cpes` varchar(255) DEFAULT NULL,
  `dev_services` varchar(255) DEFAULT NULL,
  `dev_extrainfos` varchar(255) DEFAULT NULL,
  `update_time` varchar(45) NOT NULL,
  PRIMARY KEY (`dev_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `devs`
--

LOCK TABLES `devs` WRITE;
/*!40000 ALTER TABLE `devs` DISABLE KEYS */;
INSERT INTO `devs` VALUES (1,'117.34.14.240','','up','[80, 443]',NULL,'[\'\', \'\']','[\'tcpwrapped\', \'tcpwrapped\']',NULL,'Wed Sep  5 10:55:41 2018'),(2,'123.58.182.251','','up','[80, 443]',NULL,'[\'\', \'\']','[\'tcpwrapped\', \'tcpwrapped\']',NULL,'Wed Sep  5 11:03:20 2018'),(3,'123.58.182.252','','up','[80, 443]',NULL,'[\'\', \'\']','[\'tcpwrapped\', \'tcpwrapped\']',NULL,'Wed Sep  5 11:03:20 2018'),(4,'112.74.133.190','null','unknown','[]','[]','[]','[]','[]','2018-09-13 02:26:36'),(5,'112.74.133.190','null','up','[\'42\', \'80\', \'135\', \'139\', \'445\', \'4444\', \'6666\', \'8009\', \'8011\', \'8080\']','[\'filtered\', \'open\', \'filtered\', \'filtered\', \'filtered\', \'filtered\', \'open\', \'open\', \'open\', \'open\']','[\'None\', \'cpe:/a:igor_sysoev:nginx:1.8.0\', \'None\', \'None\', \'None\', \'None\', \'cpe:/a:openbsd:openssh:6.6.1\', \'None\', \'None\', \'cpe:/a:apache:coyote_http_connector:1.1\']','[\'nameserver\', \'http\', \'msrpc\', \'netbios-ssn\', \'microsoft-ds\', \'krb524\', \'ssh\', \'ajp13\', \'unknown\', \'http\']','[\'protocol 2.0\', \'Protocol v1.3\']','2018-09-13 02:29:42'),(6,'112.74.133.190','null','up','[\'42\', \'80\', \'135\', \'139\', \'445\', \'4444\', \'6666\', \'8009\', \'8011\', \'8080\']','[\'filtered\', \'open\', \'filtered\', \'filtered\', \'filtered\', \'filtered\', \'open\', \'open\', \'open\', \'open\']','[\'None\', \'cpe:/a:igor_sysoev:nginx:1.8.0\', \'None\', \'None\', \'None\', \'None\', \'cpe:/a:openbsd:openssh:6.6.1\', \'None\', \'None\', \'cpe:/a:apache:coyote_http_connector:1.1\']','[\'nameserver\', \'http\', \'msrpc\', \'netbios-ssn\', \'microsoft-ds\', \'krb524\', \'ssh\', \'ajp13\', \'unknown\', \'http\']','[\'protocol 2.0\', \'Protocol v1.3\']','2018-09-13 04:15:29'),(7,'112.74.133.190','[\'www.moonbuy.cn\', \'tanzhouedu.com\', \'www.tanzhouedu.com\', \'bbs.tanzhouedu.com\', \'ke.tanzhouedu.com\', \'moonbuy.cn\']','up','[\'42\', \'80\', \'135\', \'139\', \'445\', \'4444\', \'6666\', \'8009\', \'8011\', \'8080\']','[\'filtered\', \'open\', \'filtered\', \'filtered\', \'filtered\', \'filtered\', \'open\', \'open\', \'open\', \'open\']','[\'None\', \'cpe:/a:igor_sysoev:nginx:1.8.0\', \'None\', \'None\', \'None\', \'None\', \'cpe:/a:openbsd:openssh:6.6.1\', \'None\', \'None\', \'cpe:/a:apache:coyote_http_connector:1.1\']','[\'nameserver\', \'http\', \'msrpc\', \'netbios-ssn\', \'microsoft-ds\', \'krb524\', \'ssh\', \'ajp13\', \'unknown\', \'http\']','[\'protocol 2.0\', \'Protocol v1.3\']','2018-09-13 17:53:58');
/*!40000 ALTER TABLE `devs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-13 18:02:15
