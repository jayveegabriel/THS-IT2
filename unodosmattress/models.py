from django.db import models
import datetime

# Create your models here.
#class Ref_HeartRate(models.Model):
#	idRef_HeartRate = models.AutoField(primary_key=True)
#	name = models.CharField(max_length=45)
#	minHeartRate = models.IntegerField(default=0)
#	maxHeartRate = models.IntegerField(default=0)

# class Ref_BedStatus(models.Model):
# 	idRef_BedStatus = models.AutoField(primary_key=True)
# 	name = models.CharField(max_length=45)

class Ref_Temp(models.Model):
	idRef_Temp = models.AutoField(primary_key=True)
	name = models.CharField(max_length=45)
	minTemp = models.IntegerField(default=0)
	maxTemp = models.IntegerField(default=0)

# class Ref_PatientStatus(models.Model):
# 	idRef_PatientStatus = models.AutoField(primary_key=True)
# 	name = models.CharField(max_length=45)


class Beds(models.Model):
	idBeds = models.AutoField(primary_key=True)
	bedNumber = models.IntegerField(default=0)
	bedStatus = models.CharField(max_length=45)


class Patient(models.Model):
	idPatient = models.AutoField(primary_key=True)
	firstName = models.CharField(max_length=45)
	middleName = models.CharField(max_length=45)
	lastName = models.CharField(max_length=45)
	birthDate = models.DateField()
	religion = models.CharField(max_length=45)
	minTemp = models.FloatField(default=0)
	maxTemp = models.FloatField(default=0)
	minHeartRate = models.IntegerField(default=0)
	maxHeartRate = models.IntegerField(default=0)
	contactperson = models.CharField(max_length=100, null=True)
	contactNum = models.CharField(max_length=11) #changethis
	bedNumber = models.ForeignKey(Beds, on_delete=models.CASCADE)
	status = models.CharField(max_length=45)

class Position(models.Model):
	idPosition = models.AutoField(primary_key=True)
	position = models.CharField(max_length=45)
	time = models.TimeField()
	date = models.DateField()
	idPatient = models.ForeignKey(Patient, on_delete=models.CASCADE)


class Temperature(models.Model):
	idTemperature = models.AutoField(primary_key=True)
	temperature = models.FloatField(default=0)
	time = models.TimeField()
	date = models.DateField()
	idPatient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	# idRef = models.ForeignKey(Ref_Temp, on_delete=models.CASCADE)


class HeartRate(models.Model):
	idHeartRate = models.AutoField(primary_key=True)
	heartRate = models.FloatField(default=0)
	time = models.TimeField()
	date = models.DateField()
	idPatient =  models.ForeignKey(Patient, on_delete=models.CASCADE)
#	idRefHeart = models.ForeignKey(Ref_HeartRate, on_delete=models.CASCADE)

class TemperatureEveryMinute(models.Model):
	idTemperature = models.AutoField(primary_key=True)
	temperature = models.FloatField(default=0)
	time = models.TimeField()
	date = models.DateField()
	idPatient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	# idRef = models.ForeignKey(Ref_Temp, on_delete=models.CASCADE)


class HeartRateEveryMinute(models.Model):
	idHeartRate = models.AutoField(primary_key=True)
	heartRate = models.FloatField(default=0)
	time = models.TimeField()
	date = models.DateField()
	idPatient =  models.ForeignKey(Patient, on_delete=models.CASCADE)
#	idRefHeart = models.ForeignKey(Ref_HeartRate, on_delete=models.CASCADE)

class Doctor(models.Model):
	idDoctor = models.AutoField(primary_key=True)
	firstName = models.CharField(max_length=45)
	middleName = models.CharField(max_length=45)
	lastName = models.CharField(max_length=45)
	contactNum = models.CharField(max_length=11) #changethis
	username = models.CharField(max_length=45)
	password = models.CharField(max_length=45)
	rfid = models.CharField(max_length=30)
	accountStatus = models.CharField(max_length=45, default="Active")


class Patient_Doctors(models.Model):
	#patientNumber = models.IntegerField(default=0)
	#doctorsID = models.IntegerField(default=0)
	Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

class Patient_Table(models.Model):
	idPatientTable = models.AutoField(primary_key=True)
	idPatient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	idBeds = models.ForeignKey(Beds, on_delete=models.CASCADE)


class Employee(models.Model):
	idEmployee = models.AutoField(primary_key=True)
	firstName = models.CharField(max_length=45)
	middleName = models.CharField(max_length=45)
	lastName = models.CharField(max_length=45)
	contactNum = models.CharField(max_length=11) #changethis
	username = models.CharField(max_length=45)
	password = models.CharField(max_length=45)
	usertype = models.CharField(max_length=45)
	rfid = models.CharField(max_length=30, null = True)
	accountStatus = models.CharField(max_length=45, default="Active")

class RFID(models.Model):
	idRFID = models.AutoField(primary_key=True)
	RFIDnumber = models.CharField(max_length=30)

class News(models.Model):
	idNews = models.AutoField(primary_key=True)
	body = models.TextField()
	date = models.DateField()
	time = models.TimeField()
	idPatient = models.ForeignKey(Patient, on_delete=models.CASCADE, null = True)


class Notification(models.Model):
	idNotification = models.AutoField(primary_key=True)
	date = models.DateField()	
	time = models.TimeField()
	bedNumber = models.IntegerField()
	body = models.CharField(max_length=100)
	

