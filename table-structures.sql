# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.23)
# Database: playground
# Generation Time: 2020-04-24 05:57:38 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table cotton_auvik_alerts_critical
# ------------------------------------------------------------

DROP TABLE IF EXISTS `cotton_auvik_alerts_critical`;

CREATE TABLE `cotton_auvik_alerts_critical` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `severity` text,
  `status` text,
  `alertName` text,
  `detectedOn` text,
  `enity` text,
  `description` text,
  `relatedAlert` text,
  `dismissed` text,
  `externalTicketId` text,
  `dispatched` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `cotton_auvik_alerts_critical` WRITE;
/*!40000 ALTER TABLE `cotton_auvik_alerts_critical` DISABLE KEYS */;

INSERT INTO `cotton_auvik_alerts_critical` (`id`, `severity`, `status`, `alertName`, `detectedOn`, `enity`, `description`, `relatedAlert`, `dismissed`, `externalTicketId`, `dispatched`)
VALUES
	(1,'Critical','Created','Network Element Offline','2020/04/22 01:31:16','Dell-SWITCH','This network element has gone offline','No Related Event','Active',' ','Yes'),
	(2,'Critical','Created','Network Element Offline','2020/04/22 01:31:16','Dell-SWITCH Member 2','This network element has gone offline','No Related Event','Active',' ','Yes'),
	(3,'Critical','Created','Network Element Offline','2020/04/22 01:31:16','Dell-SWITCH Member 1','This network element has gone offline','No Related Event','Active',' ','Yes');

/*!40000 ALTER TABLE `cotton_auvik_alerts_critical` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table cotton_auvik_alerts_emergency
# ------------------------------------------------------------

DROP TABLE IF EXISTS `cotton_auvik_alerts_emergency`;

CREATE TABLE `cotton_auvik_alerts_emergency` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `severity` text,
  `status` text,
  `alertName` text,
  `detectedOn` text,
  `enity` text,
  `description` text,
  `relatedAlert` text,
  `dismissed` text,
  `externalTicketId` text,
  `dispatched` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table cotton_auvik_alerts_informational
# ------------------------------------------------------------

DROP TABLE IF EXISTS `cotton_auvik_alerts_informational`;

CREATE TABLE `cotton_auvik_alerts_informational` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `severity` text,
  `status` text,
  `alertName` text,
  `detectedOn` text,
  `enity` text,
  `description` text,
  `relatedAlert` text,
  `dismissed` text,
  `externalTicketId` text,
  `dispatched` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `cotton_auvik_alerts_informational` WRITE;
/*!40000 ALTER TABLE `cotton_auvik_alerts_informational` DISABLE KEYS */;

INSERT INTO `cotton_auvik_alerts_informational` (`id`, `severity`, `status`, `alertName`, `detectedOn`, `enity`, `description`, `relatedAlert`, `dismissed`, `externalTicketId`, `dispatched`)
VALUES
	(1,'Informational','Created','Trunk Port Not Shared','2020/04/10 16:26:40','7250-DUN-SM-L1','Trunk ethernet port GigabitEthernet1/1/5 [offline] on device 7250-DUN-SM-L1 VLAN 100 is not shared by more than one VLAN so it may not need to be a trunk','No Related Event','Active',' ','Yes'),
	(2,'Informational','Created','Trunk Port Not Shared','2020/04/10 16:26:40','7250-DUN-SM-L1','Trunk ethernet port GigabitEthernet1/1/29 on device 7250-DUN-SM-L1 VLAN 50 is not shared by more than one VLAN so it may not need to be a trunk','No Related Event','Active',' ','Yes'),
	(3,'Informational','Created','Trunk Port Not Shared','2020/04/10 16:26:40','7250-DUN-SM-L1','Trunk ethernet port GigabitEthernet1/1/47 on device 7250-DUN-SM-L1 VLAN 2000 is not shared by more than one VLAN so it may not need to be a trunk','No Related Event','Active',' ','Yes'),
	(4,'Informational','Created','Trunk Port Not Shared','2020/04/10 16:26:40','7250-DUN-SM-L1','Trunk ethernet port GigabitEthernet1/1/40 on device 7250-DUN-SM-L1 VLAN 2000 is not shared by more than one VLAN so it may not need to be a trunk','No Related Event','Active',' ','Yes'),
	(5,'Informational','Created','Different VLAN Number','2020/04/10 16:26:40','7250-WAL-SM-L1','Connected interfaces have different VLAN numbers: Trunk ethernet port 10GigabitEthernet1/2/2 on device 7250-WAL-SM-L1 VLANs 26-29,40,50,60,100,1010,2000 is physically connected to Trunk ethernet port 10GigabitEthernet1/2/2 on device 7250-DUN-SM-L1 VLANs 26-28,40,50,60,100,1010,1020,2000','No Related Event','Active',' ','Yes'),
	(6,'Informational','Created','Trunk Port Not Shared','2020/04/10 15:50:50','CEC-FW-P','Trunk ethernet port internal4 on device CEC-FW-P VLAN 100 is not shared by more than one VLAN so it may not need to be a trunk','No Related Event','Active',' ','Yes'),
	(7,'Informational','Created','Trunk Port Not Shared','2020/04/10 15:50:50','CEC-FW-P','Trunk ethernet port internal2 on device CEC-FW-P VLAN 40 is not shared by more than one VLAN so it may not need to be a trunk','No Related Event','Active',' ','Yes'),
	(8,'Informational','Created','Trunk Port Not Shared','2020/04/10 14:40:39','switchcd6492','Trunk ethernet port gigabitethernet3/1/24 on device switchcd6492 VLAN 50 is not shared by more than one VLAN so it may not need to be a trunk','No Related Event','Active',' ','Yes'),
	(9,'Informational','Created','Trunk Port Not Shared','2020/04/10 14:40:39','switchcd6492','Trunk ethernet port gigabitethernet3/1/5 on device switchcd6492 VLAN 60 is not shared by more than one VLAN so it may not need to be a trunk','No Related Event','Active',' ','Yes'),
	(10,'Informational','Created','Trunk Port Not Shared','2020/04/10 14:24:27','7250-WAL-SM-L1','Trunk ethernet port 10GigabitEthernet1/2/7 [offline] on device 7250-WAL-SM-L1 VLAN 198 is not shared by more than one VLAN so it may not need to be a trunk','No Related Event','Active',' ','Yes'),
	(11,'Informational','Created','Trunk Port Not Shared','2020/04/10 14:24:27','7250-WAL-SM-L1','Trunk ethernet port GigabitEthernet1/1/12 on device 7250-WAL-SM-L1 VLAN 50 is not shared by more than one VLAN so it may not need to be a trunk','No Related Event','Active',' ','Yes'),
	(12,'Informational','Created','Trunk Port Not Shared','2020/04/10 14:24:27','7250-WAL-SM-L1','Trunk ethernet port GigabitEthernet1/1/42 on device 7250-WAL-SM-L1 VLAN 60 is not shared by more than one VLAN so it may not need to be a trunk','No Related Event','Active',' ','Yes'),
	(13,'Informational','Created','Trunk Port Not Shared','2020/04/10 14:24:27','7250-WAL-SM-L1','Trunk ethernet port GigabitEthernet1/1/2 on device 7250-WAL-SM-L1 VLAN 40 is not shared by more than one VLAN so it may not need to be a trunk','No Related Event','Active',' ','Yes'),
	(14,'Informational','Created','Trunk Port Not Shared','2020/04/10 14:24:27','7250-WAL-SM-L2','Trunk ethernet port 10GigabitEthernet1/2/6 [offline] on device 7250-WAL-SM-L2 VLAN 1010 is not shared by more than one VLAN so it may not need to be a trunk','No Related Event','Active',' ','Yes');

/*!40000 ALTER TABLE `cotton_auvik_alerts_informational` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table cotton_auvik_alerts_paused
# ------------------------------------------------------------

DROP TABLE IF EXISTS `cotton_auvik_alerts_paused`;

CREATE TABLE `cotton_auvik_alerts_paused` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `severity` text,
  `alertName` text,
  `enity` text,
  `numOfTriggers` text,
  `pauseWindowLength` text,
  `initiatedBy` text,
  `pauseStart` text,
  `scheduledPauseEnd` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `cotton_auvik_alerts_paused` WRITE;
/*!40000 ALTER TABLE `cotton_auvik_alerts_paused` DISABLE KEYS */;

INSERT INTO `cotton_auvik_alerts_paused` (`id`, `severity`, `alertName`, `enity`, `numOfTriggers`, `pauseWindowLength`, `initiatedBy`, `pauseStart`, `scheduledPauseEnd`)
VALUES
	(1,'Warning','Auvik Collector Disconnected','Auvik collector','Manually paused','Manually paused','Travis Cleek','2020/03/12 17:07:54','Indefinitely');

/*!40000 ALTER TABLE `cotton_auvik_alerts_paused` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table cotton_auvik_alerts_warning
# ------------------------------------------------------------

DROP TABLE IF EXISTS `cotton_auvik_alerts_warning`;

CREATE TABLE `cotton_auvik_alerts_warning` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `severity` text,
  `status` text,
  `alertName` text,
  `detectedOn` text,
  `enity` text,
  `description` text,
  `relatedAlert` text,
  `dismissed` text,
  `externalTicketId` text,
  `dispatched` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `cotton_auvik_alerts_warning` WRITE;
/*!40000 ALTER TABLE `cotton_auvik_alerts_warning` DISABLE KEYS */;

INSERT INTO `cotton_auvik_alerts_warning` (`id`, `severity`, `status`, `alertName`, `detectedOn`, `enity`, `description`, `relatedAlert`, `dismissed`, `externalTicketId`, `dispatched`)
VALUES
	(1,'Warning','Created','Printer - Low Paper','2020/04/23 17:03:37','6513','This printer is reporting a low paper level','No Related Event','Active',' ','Yes'),
	(2,'Warning','Created','Interface Status Mismatch','2020/04/22 00:10:12','Dell-SWITCH','Interface Unit: 2 Slot: 0 Port: 17 10G - Level (description not set) on Dell-SWITCH is administratively Up and has gone Down. It\'s connected to gigabitethernet3/1/42 on switchcd6492.','No Related Event','Active',' ','Yes'),
	(3,'Warning','Created','Configuration Polling','2020/04/21 11:00:00','CEC-FW-P','We\'ve been unable to poll this device for configuration details since Mon Apr 20 14:42:05 UTC 2020','No Related Event','Active',' ','Yes'),
	(4,'Warning','Created','Printer - Low Ink Level','2020/04/17 16:21:27','Device@10.38.23.80','This printer is reporting an ink percentage of 8% for Transfer Roller Unit','No Related Event','Active',' ','Yes'),
	(5,'Warning','Created','Printer - Low Ink Level','2020/04/17 16:21:26','Device@10.38.23.80','This printer is reporting an ink percentage of 0% for Developer Cartridge','No Related Event','Active',' ','Yes'),
	(6,'Warning','Created','Printer - Out of Ink','2020/04/17 16:21:26','Device@10.38.23.80','This printer is reporting that it\'s out of Developer Cartridge','No Related Event','Active',' ','Yes'),
	(7,'Warning','Created','Printer - Low Paper','2020/04/17 16:21:25','Device@10.38.23.80','This printer is reporting a low paper level','No Related Event','Active',' ','Yes'),
	(8,'Warning','Created','Printer - Out of Ink','2020/04/13 12:01:01','ET0021B749B133','This printer is reporting that it\'s out of Maintenance Kit','No Related Event','Active',' ','Yes'),
	(9,'Warning','Created','Printer - Low Ink Level','2020/04/13 12:01:01','ET0021B749B133','This printer is reporting an ink percentage of 0% for Maintenance Kit','No Related Event','Active',' ','Yes'),
	(10,'Warning','Created','Printer - Low Paper','2020/03/26 14:33:48','KMB99D37.local.','This printer is reporting a low paper level','No Related Event','Active',' ','Yes'),
	(11,'Warning','Created','Printer - Low Ink Level','2020/03/14 13:51:29','ET0021B79D3E67','This printer is reporting an ink percentage of 12% for Imaging Unit','No Related Event','Active',' ','Yes'),
	(12,'Warning','Created','Printer - Low Ink Level','2020/03/14 01:20:45','ET0021B71D4910','This printer is reporting an ink percentage of 16% for Black Toner','No Related Event','Active',' ','Yes');

/*!40000 ALTER TABLE `cotton_auvik_alerts_warning` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table cotton_auvik_internet_connections
# ------------------------------------------------------------

DROP TABLE IF EXISTS `cotton_auvik_internet_connections`;

CREATE TABLE `cotton_auvik_internet_connections` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` text,
  `highLow` text,
  `average` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `cotton_auvik_internet_connections` WRITE;
/*!40000 ALTER TABLE `cotton_auvik_internet_connections` DISABLE KEYS */;

INSERT INTO `cotton_auvik_internet_connections` (`id`, `name`, `highLow`, `average`)
VALUES
	(1,'internal1 on CEC-FW-P','2.1 Mbit/s1.7 Mbit/s','1.8 Mbit/s');

/*!40000 ALTER TABLE `cotton_auvik_internet_connections` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table cotton_auvik_top_device_usage
# ------------------------------------------------------------

DROP TABLE IF EXISTS `cotton_auvik_top_device_usage`;

CREATE TABLE `cotton_auvik_top_device_usage` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` text,
  `useage` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table cotton_auvik_top_device_utilization
# ------------------------------------------------------------

DROP TABLE IF EXISTS `cotton_auvik_top_device_utilization`;

CREATE TABLE `cotton_auvik_top_device_utilization` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` text,
  `cpu` text,
  `memory` text,
  `storage` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `cotton_auvik_top_device_utilization` WRITE;
/*!40000 ALTER TABLE `cotton_auvik_top_device_utilization` DISABLE KEYS */;

INSERT INTO `cotton_auvik_top_device_utilization` (`id`, `name`, `cpu`, `memory`, `storage`)
VALUES
	(1,'switchcd6492','70.50%','0.00%','0.00%'),
	(2,'auvik-virtual-appliance','7.42%','88.71%','34.80%'),
	(3,'Veeam','5.14%','43.97%','63.33%'),
	(4,'cotton-fsm-collector01.ad.skyhelm.com','4.05%','2.59%','32.86%'),
	(5,'AIOneHost','3.68%','31.59%','23.31%'),
	(6,'Duncan','2.00%','65.44%','0.00%'),
	(7,'7250-WAL-SM-L1','1.00%','17.84%','0.00%');

/*!40000 ALTER TABLE `cotton_auvik_top_device_utilization` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
