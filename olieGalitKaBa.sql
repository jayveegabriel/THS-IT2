auth_userunodosmattress_patientunodosmattress_patient-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: mattress
-- ------------------------------------------------------
-- Server version	5.7.17-log

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=89 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add beds',1,'add_beds'),(2,'Can change beds',1,'change_beds'),(3,'Can delete beds',1,'delete_beds'),(4,'Can view beds',1,'view_beds'),(5,'Can add doctor',2,'add_doctor'),(6,'Can change doctor',2,'change_doctor'),(7,'Can delete doctor',2,'delete_doctor'),(8,'Can view doctor',2,'view_doctor'),(9,'Can add employee',3,'add_employee'),(10,'Can change employee',3,'change_employee'),(11,'Can delete employee',3,'delete_employee'),(12,'Can view employee',3,'view_employee'),(13,'Can add heart rate',4,'add_heartrate'),(14,'Can change heart rate',4,'change_heartrate'),(15,'Can delete heart rate',4,'delete_heartrate'),(16,'Can view heart rate',4,'view_heartrate'),(17,'Can add heart rate every minute',5,'add_heartrateeveryminute'),(18,'Can change heart rate every minute',5,'change_heartrateeveryminute'),(19,'Can delete heart rate every minute',5,'delete_heartrateeveryminute'),(20,'Can view heart rate every minute',5,'view_heartrateeveryminute'),(21,'Can add news',6,'add_news'),(22,'Can change news',6,'change_news'),(23,'Can delete news',6,'delete_news'),(24,'Can view news',6,'view_news'),(25,'Can add notification',7,'add_notification'),(26,'Can change notification',7,'change_notification'),(27,'Can delete notification',7,'delete_notification'),(28,'Can view notification',7,'view_notification'),(29,'Can add patient',8,'add_patient'),(30,'Can change patient',8,'change_patient'),(31,'Can delete patient',8,'delete_patient'),(32,'Can view patient',8,'view_patient'),(33,'Can add patient_ doctors',9,'add_patient_doctors'),(34,'Can change patient_ doctors',9,'change_patient_doctors'),(35,'Can delete patient_ doctors',9,'delete_patient_doctors'),(36,'Can view patient_ doctors',9,'view_patient_doctors'),(37,'Can add patient_ table',10,'add_patient_table'),(38,'Can change patient_ table',10,'change_patient_table'),(39,'Can delete patient_ table',10,'delete_patient_table'),(40,'Can view patient_ table',10,'view_patient_table'),(41,'Can add position',11,'add_position'),(42,'Can change position',11,'change_position'),(43,'Can delete position',11,'delete_position'),(44,'Can view position',11,'view_position'),(45,'Can add ref_ temp',12,'add_ref_temp'),(46,'Can change ref_ temp',12,'change_ref_temp'),(47,'Can delete ref_ temp',12,'delete_ref_temp'),(48,'Can view ref_ temp',12,'view_ref_temp'),(49,'Can add rfid',13,'add_rfid'),(50,'Can change rfid',13,'change_rfid'),(51,'Can delete rfid',13,'delete_rfid'),(52,'Can view rfid',13,'view_rfid'),(53,'Can add room',14,'add_room'),(54,'Can change room',14,'change_room'),(55,'Can delete room',14,'delete_room'),(56,'Can view room',14,'view_room'),(57,'Can add temperature',15,'add_temperature'),(58,'Can change temperature',15,'change_temperature'),(59,'Can delete temperature',15,'delete_temperature'),(60,'Can view temperature',15,'view_temperature'),(61,'Can add temperature every minute',16,'add_temperatureeveryminute'),(62,'Can change temperature every minute',16,'change_temperatureeveryminute'),(63,'Can delete temperature every minute',16,'delete_temperatureeveryminute'),(64,'Can view temperature every minute',16,'view_temperatureeveryminute'),(65,'Can add log entry',17,'add_logentry'),(66,'Can change log entry',17,'change_logentry'),(67,'Can delete log entry',17,'delete_logentry'),(68,'Can view log entry',17,'view_logentry'),(69,'Can add permission',18,'add_permission'),(70,'Can change permission',18,'change_permission'),(71,'Can delete permission',18,'delete_permission'),(72,'Can view permission',18,'view_permission'),(73,'Can add group',19,'add_group'),(74,'Can change group',19,'change_group'),(75,'Can delete group',19,'delete_group'),(76,'Can view group',19,'view_group'),(77,'Can add user',20,'add_user'),(78,'Can change user',20,'change_user'),(79,'Can delete user',20,'delete_user'),(80,'Can view user',20,'view_user'),(81,'Can add content type',21,'add_contenttype'),(82,'Can change content type',21,'change_contenttype'),(83,'Can delete content type',21,'delete_contenttype'),(84,'Can view content type',21,'view_contenttype'),(85,'Can add session',22,'add_session'),(86,'Can change session',22,'change_session'),(87,'Can delete session',22,'delete_session'),(88,'Can view session',22,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (17,'admin','logentry'),(19,'auth','group'),(18,'auth','permission'),(20,'auth','user'),(21,'contenttypes','contenttype'),(22,'sessions','session'),(1,'unodosmattress','beds'),(2,'unodosmattress','doctor'),(3,'unodosmattress','employee'),(4,'unodosmattress','heartrate'),(5,'unodosmattress','heartrateeveryminute'),(6,'unodosmattress','news'),(7,'unodosmattress','notification'),(8,'unodosmattress','patient'),(9,'unodosmattress','patient_doctors'),(10,'unodosmattress','patient_table'),(11,'unodosmattress','position'),(12,'unodosmattress','ref_temp'),(13,'unodosmattress','rfid'),(14,'unodosmattress','room'),(15,'unodosmattress','temperature'),(16,'unodosmattress','temperatureeveryminute');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-02-23 10:15:33.911650'),(2,'auth','0001_initial','2019-02-23 10:15:43.993380'),(3,'admin','0001_initial','2019-02-23 10:15:46.385550'),(4,'admin','0002_logentry_remove_auto_add','2019-02-23 10:15:46.416796'),(5,'admin','0003_logentry_add_action_flag_choices','2019-02-23 10:15:46.448074'),(6,'contenttypes','0002_remove_content_type_name','2019-02-23 10:15:47.729604'),(7,'auth','0002_alter_permission_name_max_length','2019-02-23 10:15:48.603783'),(8,'auth','0003_alter_user_email_max_length','2019-02-23 10:15:50.119210'),(9,'auth','0004_alter_user_username_opts','2019-02-23 10:15:50.150298'),(10,'auth','0005_alter_user_last_login_null','2019-02-23 10:15:50.947270'),(11,'auth','0006_require_contenttypes_0002','2019-02-23 10:15:50.993852'),(12,'auth','0007_alter_validators_add_error_messages','2019-02-23 10:15:51.009986'),(13,'auth','0008_alter_user_username_max_length','2019-02-23 10:15:51.733445'),(14,'auth','0009_alter_user_last_name_max_length','2019-02-23 10:15:52.592660'),(15,'sessions','0001_initial','2019-02-23 10:15:53.108123'),(16,'unodosmattress','0001_initial','2019-02-23 10:16:14.000992'),(17,'unodosmattress','0002_remove_patient_religion','2019-02-24 17:41:50.710063'),(18,'unodosmattress','0003_patient_restrictions','2019-02-24 17:54:29.249326'),(19,'unodosmattress','0004_patient_count','2019-02-26 06:15:56.804055');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('219kmuv82427wvflv99qy25l144z9r3s','MmQyNTQ4YjAwOWJkMDRiYzdkOWZlNDEwMzhmNzUxODVkYjUyYzIzZjp7InBvc2l0aW9uIjoiQURNSU4ifQ==','2019-03-09 13:44:37.541825'),('7dbu1g6g7zjv2pjz4y2itrr5x066we3i','MmQyNTQ4YjAwOWJkMDRiYzdkOWZlNDEwMzhmNzUxODVkYjUyYzIzZjp7InBvc2l0aW9uIjoiQURNSU4ifQ==','2019-03-09 13:25:47.172358'),('90txevuiuf8fr5penh5mvs1pwgekh9if','MmQyNTQ4YjAwOWJkMDRiYzdkOWZlNDEwMzhmNzUxODVkYjUyYzIzZjp7InBvc2l0aW9uIjoiQURNSU4ifQ==','2019-03-09 13:25:46.733144'),('aac3cevsy40n9txual8q79hjss8x79vk','MGIxYTNjOThlZmRhMWRiNzAzZDJhYzg3NGE1ZTAxYzA4MzRjOWU3OTp7InBvc2l0aW9uIjoiRE9DVE9SIiwiaWQiOjF9','2019-03-12 06:51:30.691563'),('b85xb63k18f0ti6bc1ideer2u4q2dsm9','MmQyNTQ4YjAwOWJkMDRiYzdkOWZlNDEwMzhmNzUxODVkYjUyYzIzZjp7InBvc2l0aW9uIjoiQURNSU4ifQ==','2019-03-09 13:25:47.285527'),('jrtvfl3leoojuvr3d92oai62tejysogc','MmQyNTQ4YjAwOWJkMDRiYzdkOWZlNDEwMzhmNzUxODVkYjUyYzIzZjp7InBvc2l0aW9uIjoiQURNSU4ifQ==','2019-03-09 13:25:46.598390');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unodosmattress_beds`
--

DROP TABLE IF EXISTS `unodosmattress_beds`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `unodosmattress_beds` (
  `idBeds` int(11) NOT NULL AUTO_INCREMENT,
  `bedNumber` int(11) NOT NULL,
  `bedStatus` varchar(45) NOT NULL,
  `idRoom_id` int(11) NOT NULL,
  PRIMARY KEY (`idBeds`),
  KEY `unodosmattress_beds_idRoom_id_700cf650_fk_unodosmat` (`idRoom_id`),
  CONSTRAINT `unodosmattress_beds_idRoom_id_700cf650_fk_unodosmat` FOREIGN KEY (`idRoom_id`) REFERENCES `unodosmattress_room` (`idRoom`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unodosmattress_beds`
--

LOCK TABLES `unodosmattress_beds` WRITE;
/*!40000 ALTER TABLE `unodosmattress_beds` DISABLE KEYS */;
INSERT INTO `unodosmattress_beds` VALUES (1,1,'Available',1),(2,2,'Unavailable',1),(3,3,'Occupied',1);
/*!40000 ALTER TABLE `unodosmattress_beds` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unodosmattress_doctor`
--

DROP TABLE IF EXISTS `unodosmattress_doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `unodosmattress_doctor` (
  `idDoctor` int(11) NOT NULL AUTO_INCREMENT,
  `firstName` varchar(45) NOT NULL,
  `middleName` varchar(45) NOT NULL,
  `lastName` varchar(45) NOT NULL,
  `contactNum` varchar(11) NOT NULL,
  `username` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `rfid` varchar(30) NOT NULL,
  `accountStatus` varchar(45) NOT NULL,
  PRIMARY KEY (`idDoctor`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unodosmattress_doctor`
--

LOCK TABLES `unodosmattress_doctor` WRITE;
/*!40000 ALTER TABLE `unodosmattress_doctor` DISABLE KEYS */;
INSERT INTO `unodosmattress_doctor` VALUES (1,'Nicole','Mariano','Domingo','9293929302','Doctor','123','','Active');
/*!40000 ALTER TABLE `unodosmattress_doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unodosmattress_employee`
--

DROP TABLE IF EXISTS `unodosmattress_employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `unodosmattress_employee` (
  `idEmployee` int(11) NOT NULL AUTO_INCREMENT,
  `firstName` varchar(45) NOT NULL,
  `middleName` varchar(45) NOT NULL,
  `lastName` varchar(45) NOT NULL,
  `contactNum` varchar(11) NOT NULL,
  `username` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `usertype` varchar(45) NOT NULL,
  `rfid` varchar(30) DEFAULT NULL,
  `accountStatus` varchar(45) NOT NULL,
  PRIMARY KEY (`idEmployee`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unodosmattress_employee`
--

LOCK TABLES `unodosmattress_employee` WRITE;
/*!40000 ALTER TABLE `unodosmattress_employee` DISABLE KEYS */;
INSERT INTO `unodosmattress_employee` VALUES (1,'Jayvee','Tomas','Gabriel','9062268410','Nurse','123','Nurse',NULL,'Active');
/*!40000 ALTER TABLE `unodosmattress_employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unodosmattress_heartrate`
--

DROP TABLE IF EXISTS `unodosmattress_heartrate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `unodosmattress_heartrate` (
  `idHeartRate` int(11) NOT NULL AUTO_INCREMENT,
  `heartRate` double NOT NULL,
  `time` time(6) NOT NULL,
  `date` date NOT NULL,
  `idPatient_id` int(11) NOT NULL,
  PRIMARY KEY (`idHeartRate`),
  KEY `unodosmattress_heart_idPatient_id_eb711523_fk_unodosmat` (`idPatient_id`),
  CONSTRAINT `unodosmattress_heart_idPatient_id_eb711523_fk_unodosmat` FOREIGN KEY (`idPatient_id`) REFERENCES `unodosmattress_patient` (`idPatient`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unodosmattress_heartrate`
--

LOCK TABLES `unodosmattress_heartrate` WRITE;
/*!40000 ALTER TABLE `unodosmattress_heartrate` DISABLE KEYS */;
INSERT INTO `unodosmattress_heartrate` VALUES (1,62,'00:00:00.000000','2019-10-10',3),(2,72,'00:00:01.000000','2019-10-10',3),(3,101,'00:00:02.000000','2019-10-10',3);
/*!40000 ALTER TABLE `unodosmattress_heartrate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unodosmattress_heartrateeveryminute`
--

DROP TABLE IF EXISTS `unodosmattress_heartrateeveryminute`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `unodosmattress_heartrateeveryminute` (
  `idHeartRate` int(11) NOT NULL AUTO_INCREMENT,
  `heartRate` double NOT NULL,
  `time` time(6) NOT NULL,
  `date` date NOT NULL,
  `idPatient_id` int(11) NOT NULL,
  PRIMARY KEY (`idHeartRate`),
  KEY `unodosmattress_heart_idPatient_id_38b966f6_fk_unodosmat` (`idPatient_id`),
  CONSTRAINT `unodosmattress_heart_idPatient_id_38b966f6_fk_unodosmat` FOREIGN KEY (`idPatient_id`) REFERENCES `unodosmattress_patient` (`idPatient`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unodosmattress_heartrateeveryminute`
--

LOCK TABLES `unodosmattress_heartrateeveryminute` WRITE;
/*!40000 ALTER TABLE `unodosmattress_heartrateeveryminute` DISABLE KEYS */;
INSERT INTO `unodosmattress_heartrateeveryminute` VALUES (1,62,'00:00:00.000000','2019-10-10',3),(2,72,'00:00:01.000000','2019-10-10',3);
/*!40000 ALTER TABLE `unodosmattress_heartrateeveryminute` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unodosmattress_news`
--

DROP TABLE IF EXISTS `unodosmattress_news`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `unodosmattress_news` (
  `idNews` int(11) NOT NULL AUTO_INCREMENT,
  `body` longtext NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `idPatient_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`idNews`),
  KEY `unodosmattress_news_idPatient_id_6da620cf_fk_unodosmat` (`idPatient_id`),
  CONSTRAINT `unodosmattress_news_idPatient_id_6da620cf_fk_unodosmat` FOREIGN KEY (`idPatient_id`) REFERENCES `unodosmattress_patient` (`idPatient`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unodosmattress_news`
--

LOCK TABLES `unodosmattress_news` WRITE;
/*!40000 ALTER TABLE `unodosmattress_news` DISABLE KEYS */;
INSERT INTO `unodosmattress_news` VALUES (1,'Your patient, Jayvee Gabriel, is now on the bed.','2019-02-24','23:34:46.934945',3),(3,'Your patient, q qqwe, is now in the recovery room.','2019-02-25','01:47:08.713295',3),(4,'Your patient, Jayvee Gabriel, is now on the bed.','2019-02-25','16:22:04.646328',3);
/*!40000 ALTER TABLE `unodosmattress_news` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unodosmattress_notification`
--

DROP TABLE IF EXISTS `unodosmattress_notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `unodosmattress_notification` (
  `idNotification` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `bedNumber` int(11) NOT NULL,
  `body` varchar(100) NOT NULL,
  PRIMARY KEY (`idNotification`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unodosmattress_notification`
--

LOCK TABLES `unodosmattress_notification` WRITE;
/*!40000 ALTER TABLE `unodosmattress_notification` DISABLE KEYS */;
/*!40000 ALTER TABLE `unodosmattress_notification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unodosmattress_patient`
--

DROP TABLE IF EXISTS `unodosmattress_patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `unodosmattress_patient` (
  `idPatient` int(11) NOT NULL AUTO_INCREMENT,
  `firstName` varchar(45) NOT NULL,
  `middleName` varchar(45) NOT NULL,
  `lastName` varchar(45) NOT NULL,
  `birthDate` date NOT NULL,
  `minTemp` double NOT NULL,
  `maxTemp` double NOT NULL,
  `minHeartRate` int(11) NOT NULL,
  `maxHeartRate` int(11) NOT NULL,
  `contactperson` varchar(100) DEFAULT NULL,
  `contactNum` varchar(11) NOT NULL,
  `status` varchar(45) NOT NULL,
  `bedNumber_id` int(11) NOT NULL,
  `restrictions` varchar(20) NOT NULL,
  `count` int(11) NOT NULL,
  PRIMARY KEY (`idPatient`),
  KEY `unodosmattress_patie_bedNumber_id_e17a3730_fk_unodosmat` (`bedNumber_id`),
  CONSTRAINT `unodosmattress_patie_bedNumber_id_e17a3730_fk_unodosmat` FOREIGN KEY (`bedNumber_id`) REFERENCES `unodosmattress_beds` (`idBeds`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unodosmattress_patient`
--

LOCK TABLES `unodosmattress_patient` WRITE;
/*!40000 ALTER TABLE `unodosmattress_patient` DISABLE KEYS */;
INSERT INTO `unodosmattress_patient` VALUES (3,'Jayvee','Tomas','Gabriel','1111-11-11',35,37,60,100,'q','11111111111','ON BED',3,'false',0);
/*!40000 ALTER TABLE `unodosmattress_patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unodosmattress_patient_doctors`
--

DROP TABLE IF EXISTS `unodosmattress_patient_doctors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `unodosmattress_patient_doctors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Doctor_id` int(11) NOT NULL,
  `Patient_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `unodosmattress_patie_Doctor_id_f920fc8e_fk_unodosmat` (`Doctor_id`),
  KEY `unodosmattress_patie_Patient_id_3c6364be_fk_unodosmat` (`Patient_id`),
  CONSTRAINT `unodosmattress_patie_Doctor_id_f920fc8e_fk_unodosmat` FOREIGN KEY (`Doctor_id`) REFERENCES `unodosmattress_doctor` (`idDoctor`),
  CONSTRAINT `unodosmattress_patie_Patient_id_3c6364be_fk_unodosmat` FOREIGN KEY (`Patient_id`) REFERENCES `unodosmattress_patient` (`idPatient`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unodosmattress_patient_doctors`
--

LOCK TABLES `unodosmattress_patient_doctors` WRITE;
/*!40000 ALTER TABLE `unodosmattress_patient_doctors` DISABLE KEYS */;
INSERT INTO `unodosmattress_patient_doctors` VALUES (1,1,3);
/*!40000 ALTER TABLE `unodosmattress_patient_doctors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unodosmattress_patient_table`
--

DROP TABLE IF EXISTS `unodosmattress_patient_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `unodosmattress_patient_table` (
  `idPatientTable` int(11) NOT NULL AUTO_INCREMENT,
  `idBeds_id` int(11) NOT NULL,
  `idPatient_id` int(11) NOT NULL,
  PRIMARY KEY (`idPatientTable`),
  KEY `unodosmattress_patie_idBeds_id_d3ffa9b8_fk_unodosmat` (`idBeds_id`),
  KEY `unodosmattress_patie_idPatient_id_72ad5404_fk_unodosmat` (`idPatient_id`),
  CONSTRAINT `unodosmattress_patie_idBeds_id_d3ffa9b8_fk_unodosmat` FOREIGN KEY (`idBeds_id`) REFERENCES `unodosmattress_beds` (`idBeds`),
  CONSTRAINT `unodosmattress_patie_idPatient_id_72ad5404_fk_unodosmat` FOREIGN KEY (`idPatient_id`) REFERENCES `unodosmattress_patient` (`idPatient`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unodosmattress_patient_table`
--

LOCK TABLES `unodosmattress_patient_table` WRITE;
/*!40000 ALTER TABLE `unodosmattress_patient_table` DISABLE KEYS */;
INSERT INTO `unodosmattress_patient_table` VALUES (2,3,3);
/*!40000 ALTER TABLE `unodosmattress_patient_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unodosmattress_position`
--

DROP TABLE IF EXISTS `unodosmattress_position`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `unodosmattress_position` (
  `idPosition` int(11) NOT NULL AUTO_INCREMENT,
  `position` varchar(45) NOT NULL,
  `time` time(6) NOT NULL,
  `date` date NOT NULL,
  `idPatient_id` int(11) NOT NULL,
  PRIMARY KEY (`idPosition`),
  KEY `unodosmattress_posit_idPatient_id_0e64819a_fk_unodosmat` (`idPatient_id`),
  CONSTRAINT `unodosmattress_posit_idPatient_id_0e64819a_fk_unodosmat` FOREIGN KEY (`idPatient_id`) REFERENCES `unodosmattress_patient` (`idPatient`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unodosmattress_position`
--

LOCK TABLES `unodosmattress_position` WRITE;
/*!40000 ALTER TABLE `unodosmattress_position` DISABLE KEYS */;
INSERT INTO `unodosmattress_position` VALUES (1,'LEFT SIDE','00:00:00.000000','2019-10-10',3);
/*!40000 ALTER TABLE `unodosmattress_position` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unodosmattress_ref_temp`
--

DROP TABLE IF EXISTS `unodosmattress_ref_temp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `unodosmattress_ref_temp` (
  `idRef_Temp` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `minTemp` int(11) NOT NULL,
  `maxTemp` int(11) NOT NULL,
  PRIMARY KEY (`idRef_Temp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unodosmattress_ref_temp`
--

LOCK TABLES `unodosmattress_ref_temp` WRITE;
/*!40000 ALTER TABLE `unodosmattress_ref_temp` DISABLE KEYS */;
/*!40000 ALTER TABLE `unodosmattress_ref_temp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unodosmattress_rfid`
--

DROP TABLE IF EXISTS `unodosmattress_rfid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `unodosmattress_rfid` (
  `idRFID` int(11) NOT NULL AUTO_INCREMENT,
  `RFIDnumber` varchar(30) NOT NULL,
  PRIMARY KEY (`idRFID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unodosmattress_rfid`
--

LOCK TABLES `unodosmattress_rfid` WRITE;
/*!40000 ALTER TABLE `unodosmattress_rfid` DISABLE KEYS */;
INSERT INTO `unodosmattress_rfid` VALUES (1,'102 102 201 03');
/*!40000 ALTER TABLE `unodosmattress_rfid` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unodosmattress_room`
--

DROP TABLE IF EXISTS `unodosmattress_room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `unodosmattress_room` (
  `idRoom` int(11) NOT NULL AUTO_INCREMENT,
  `roomNumber` varchar(45) NOT NULL,
  PRIMARY KEY (`idRoom`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unodosmattress_room`
--

LOCK TABLES `unodosmattress_room` WRITE;
/*!40000 ALTER TABLE `unodosmattress_room` DISABLE KEYS */;
INSERT INTO `unodosmattress_room` VALUES (1,'1'),(2,'2');
/*!40000 ALTER TABLE `unodosmattress_room` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unodosmattress_temperature`
--

DROP TABLE IF EXISTS `unodosmattress_temperature`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `unodosmattress_temperature` (
  `idTemperature` int(11) NOT NULL AUTO_INCREMENT,
  `temperature` double NOT NULL,
  `time` time(6) NOT NULL,
  `date` date NOT NULL,
  `idPatient_id` int(11) NOT NULL,
  PRIMARY KEY (`idTemperature`),
  KEY `unodosmattress_tempe_idPatient_id_6efe6e0b_fk_unodosmat` (`idPatient_id`),
  CONSTRAINT `unodosmattress_tempe_idPatient_id_6efe6e0b_fk_unodosmat` FOREIGN KEY (`idPatient_id`) REFERENCES `unodosmattress_patient` (`idPatient`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unodosmattress_temperature`
--

LOCK TABLES `unodosmattress_temperature` WRITE;
/*!40000 ALTER TABLE `unodosmattress_temperature` DISABLE KEYS */;
INSERT INTO `unodosmattress_temperature` VALUES (1,36,'00:00:00.000000','2019-10-10',3);
/*!40000 ALTER TABLE `unodosmattress_temperature` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unodosmattress_temperatureeveryminute`
--

DROP TABLE IF EXISTS `unodosmattress_temperatureeveryminute`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `unodosmattress_temperatureeveryminute` (
  `idTemperature` int(11) NOT NULL AUTO_INCREMENT,
  `temperature` double NOT NULL,
  `time` time(6) NOT NULL,
  `date` date NOT NULL,
  `idPatient_id` int(11) NOT NULL,
  PRIMARY KEY (`idTemperature`),
  KEY `unodosmattress_tempe_idPatient_id_04cd43d5_fk_unodosmat` (`idPatient_id`),
  CONSTRAINT `unodosmattress_tempe_idPatient_id_04cd43d5_fk_unodosmat` FOREIGN KEY (`idPatient_id`) REFERENCES `unodosmattress_patient` (`idPatient`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unodosmattress_temperatureeveryminute`
--

LOCK TABLES `unodosmattress_temperatureeveryminute` WRITE;
/*!40000 ALTER TABLE `unodosmattress_temperatureeveryminute` DISABLE KEYS */;
/*!40000 ALTER TABLE `unodosmattress_temperatureeveryminute` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-02-26 15:36:47
