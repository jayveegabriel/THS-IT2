from django.db import models
import datetime
from django.db import connection


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


class Room(models.Model):
	idRoom = models.AutoField(primary_key=True)
	roomNumber = models.CharField(max_length=45)
	@property
	def get_beds(self):
		return Beds.objects.filter(idRoom_id=self.idRoom)

	@property
	def get_occupied_beds(self):
		return Beds.objects.filter(idRoom_id=self.idRoom,bedStatus="Occupied").values()


	@property
	def get_occupied_beds_dashboard(self):
		return Beds.objects.filter(idRoom_id=self.idRoom,bedStatus="Occupied")


	@property
	def get_occupied_size(self):
		return len(Beds.objects.filter(idRoom_id=self.idRoom,bedStatus="Occupied"))
	
	@property
	def get_available_beds(self):
		return Beds.objects.filter(idRoom_id=self.idRoom,bedStatus="Available").values()

	@property
	def get_available_size(self):
		return len(Beds.objects.filter(idRoom_id=self.idRoom,bedStatus="Available"))

	@property
	def get_unavailable_beds(self):
		return Beds.objects.filter(idRoom_id=self.idRoom,bedStatus="Unavailable").values()

	@property
	def get_unavailable_size(self):
		return len(Beds.objects.filter(idRoom_id=self.idRoom,bedStatus="Unavailable"))

	@property
	def get_all_pending_beds(self):
		return Beds.objects.filter(bedStatus="Pending")

	@property
	def get_pending_size(self):
		return len(self.get_all_pending_beds)
	
	
	



class Beds(models.Model):
	idBeds = models.AutoField(primary_key=True)
	bedNumber = models.IntegerField(default=0)
	bedStatus = models.CharField(max_length=45)
	idRoom = models.ForeignKey(Room, on_delete=models.CASCADE)

	@property
	def get_current_patient(self):
		return Patient_Table.objects.select_related("idPatient").get(idBeds=self.idBeds,idBeds__bedStatus="Occupied")

	
	


class Patient(models.Model):
	idPatient = models.AutoField(primary_key=True)
	firstName = models.CharField(max_length=45)
	middleName = models.CharField(max_length=45)
	lastName = models.CharField(max_length=45)
	birthDate = models.DateField()

	minTemp = models.FloatField(default=0)
	maxTemp = models.FloatField(default=0)
	minHeartRate = models.IntegerField(default=0)
	maxHeartRate = models.IntegerField(default=0)
	contactperson = models.CharField(max_length=100, null=True)
	contactNum = models.CharField(max_length=11) #changethis
	bedNumber = models.ForeignKey(Beds, on_delete=models.CASCADE)
	status = models.CharField(max_length=45)
	restrictions = models.CharField(max_length=20, default="false")
	countHR = models.IntegerField(default=0)
	countT = models.IntegerField(default=0)

	@property
	def get_position(self):
		return Position.objects.filter(idPatient_id = self.idPatient).select_related('idPatient').latest('date','time').position

	@property
	def get_heartrate(self):
		return HeartRate.objects.filter(idPatient_id = self.idPatient).select_related('idPatient').latest('date','time').heartRate

	@property
	def get_temperature(self):
		return Temperature.objects.filter(idPatient_id = self.idPatient).select_related('idPatient').latest('date','time').temperature
	
	@property
	def get_all_position(self):
		return Position.objects.filter(idPatient_id = self.idPatient).select_related("idPatient").order_by('date','time')


	@property
	def get_all_heartrate(self):
		return HeartRate.objects.filter(idPatient_id = self.idPatient).select_related("idPatient").order_by('date','time')


	@property
	def get_all_temperature(self):
		return Temperature.objects.filter(idPatient_id = self.idPatient).select_related("idPatient").order_by('date','time')


	@property
	def get_changes_in_position(self):
		p = self.get_all_position
		wew = []
		for x in range(1, len(p) - 1):
			

			prevTemp = p[x - 1].position
			nextTemp = p[x].position
			if prevTemp != nextTemp:
				wew.append({"idPosition":p[x].idPosition, "position":prevTemp,"time":p[x].time,"date":p[x].date})

		return wew

	@property
	def getQFifteenHeartRate(self):
		cursor = connection.cursor()
		cursor.execute("SELECT *,FLOOR(UNIX_TIMESTAMP(time)/(15*60)) as timekey FROM unodosmattress_heartrate WHERE idPatient_id = %s group by timekey",[self.pk])
		hr = cursor.fetchall()
		heartRate_list = []
		for x in range(0, len(hr)):
			heartRate_list.append({"idHeartRate":hr[x][0], "heartRate": hr[x][1],"time":hr[x][2], "date":hr[x][3], "idPatient":hr[x][4]})
		return heartRate_list
	
	
	
	@property
	def getQFifteenTemperature(self):
		cursor = connection.cursor()
		cursor.execute("SELECT *,FLOOR(UNIX_TIMESTAMP(time)/(15*60)) as timekey FROM unodosmattress_temperature WHERE idPatient_id = %s group by timekey",[self.pk])
		temp = cursor.fetchall()
		temp_list = []
		for x in range(0, len(temp)):
			temp_list.append({"idTemperature":temp[x][0], "temperature": temp[x][1],"time":temp[x][2], "date":temp[x][3], "idPatient":temp[x][4]})
		return temp_list
		

	@property
	def getQOneHeartRate(self):
		cursor = connection.cursor()
		cursor.execute("SELECT *,FLOOR(UNIX_TIMESTAMP(time)/(1*60)) as timekey FROM unodosmattress_heartrate WHERE idPatient_id = %s group by timekey",[self.pk])
		hr = cursor.fetchall()
		heartRate_list = []
		for x in range(0, len(hr)):
			heartRate_list.append({"idHeartRate":hr[x][0], "heartRate": hr[x][1],"time":hr[x][2], "date":hr[x][3], "idPatient":hr[x][4]})
		return heartRate_list
	
	@property
	def getQOneTemperature(self):
		cursor = connection.cursor()
		cursor.execute("SELECT *,FLOOR(UNIX_TIMESTAMP(time)/(11*60)) as timekey FROM unodosmattress_temperature WHERE idPatient_id = %s group by timekey",[self.pk])
		temp = cursor.fetchall()
		temp_list = []
		for x in range(0, len(temp)):
			temp_list.append({"idTemperature":temp[x][0], "temperature": temp[x][1],"time":temp[x][2], "date":temp[x][3], "idPatient":temp[x][4]})
		return temp_list
		

	

	@property
	def toCompareHR(self):


		diffMinHR = self.get_heartrate - self.minHeartRate
		diffMaxHR = self.maxHeartRate - self.get_heartrate
		if diffMinHR >= diffMaxHR:
			toCompareHR = diffMaxHR
		else:
			toCompareHR = diffMinHR

		return toCompareHR
	
	@property
	def toCompareTEMP(self):
		diffMinTEMP = self.get_temperature - self.minTemp
		diffMaxTEMP = self.maxTemp - self.get_temperature

		

		if diffMinTEMP >= diffMaxTEMP:
			toCompareTEMP = diffMaxTEMP
		else:
			toCompareTEMP = diffMinTEMP


		return toCompareTEMP

	@property
	def get_patient_condition(self):
		# normal, warning, critical
		condition = "normal"
		
		if self.toCompareTEMP < 0:
			condition = "critical"
		elif self.toCompareTEMP <= 0.3 and self.toCompareTEMP >= 0 or self.toCompareHR <= 10 and self.toCompareHR >= 0:
			condition = "warning"
		else:
			condition = "normal"
		if self.status == "STARTING":
			condition = "starting"
		return condition
	
	@property
	def get_patient_conditionHR(self):
		# normal, warning, critical
		condition = "normal"
		
		if self.toCompareHR < 0:
			condition = "critical"
		elif self.toCompareHR <= 10 and self.toCompareHR >= 0:
			condition = "warning"
		else:
			condition = "normal"
		if self.status == "STARTING":
			condition = "starting"
		return condition

	@property
	def get_patient_conditionT(self):
		# normal, warning, critical
		condition = "normal"
		
		if self.toCompareTEMP < 0:
			condition = "critical"
		elif self.toCompareTEMP <= 0.3 and self.toCompareTEMP >= 0:
			condition = "warning"
		else:
			condition = "normal"
		if self.status == "STARTING":
			condition = "starting"
		return condition
	


	

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
	idPatientDoctor = models.AutoField(primary_key=True, default=None)
	idPatient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	idDoctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

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
	
	@staticmethod
	def get_dates():
		return Notification.objects.values('date').distinct().order_by('-date')
