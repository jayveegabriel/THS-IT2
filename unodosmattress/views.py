from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.db import connection
from . models import  *
import coreapi
from threading import Timer

from rest_framework import generics
from unodosmattress.serializers import *

from rest_framework.response import Response
from rest_framework.reverse import reverse
import datetime
from django.http import JsonResponse
from django.core import serializers
from django.utils.dateparse import parse_date
import threading
import serial
import time

position = ''
isClicked = False
buttonClicked = []
notificationList = []
newNotificationList = []



def readRFID():


	arduino = serial.Serial('COM4', 9600, timeout=.1)

	store = ""
	value = ""
	while(True):
		try:
			store = arduino.readline()
			time.sleep(1)
			store = arduino.readline()
			## print(store)
			value = store.decode('utf-8')

			if value != "":
				print("HI")

				client = coreapi.Client()
				# schema = client.get("http://192.168.100.222:8000/docs")
				schema = client.get("http://192.168.100.222:8000/docs")
				action = ["rfid","create"]
				params = {
				 		"RFIDnumber": value,
				}
				result = client.action(schema,action,params=params)

		except:
			print("Cannot read arduino")



t = threading.Thread(target=readRFID)
t.start()


def ajaxGetCurrentRFIDs(request):
	temp = RFID.objects.all()

	latest = temp.latest("idRFID")

	size = len(temp)

	wew = []
	wew.append({"size":size,"RFIDnumber":latest.RFIDnumber})
	return JsonResponse(wew, safe=False)


def clickButton(request,idBed):
	b = ButtonClick(idBed)
	buttonClicked.append(b)
	notificationList.append(b)
	newNotificationList.append(b)

	return HttpResponse()


class ButtonClick:
	def __init__(self, bedNumber):
		self.bedNumber = bedNumber
		t = Timer(5.0, self.unclick)
		# t.start()
	def unclick(self):
		global buttonClicked
		buttonClicked.remove(self)
	def getBedNumber():
		return self.bedNumber

def ajaxGetClicked(request):
	global buttonClicked
	wew = []
	for x in range(0, len(buttonClicked)):
		wew.append({"bedNumber":buttonClicked[x].bedNumber	})
	return JsonResponse (wew, safe=False)

def ajaxGetNewNotifications(request):
	wew = []
	for x in range(0, len(newNotificationList)):
		wew.append({"bedNumber":newNotificationList[x].bedNumber})
	return JsonResponse(wew, safe=False)

def ajaxGetNewNotificationsSize(request):
	wew = []
	wew.append({"size":len(newNotificationList)})
	return JsonResponse(wew, safe=False)

def ajaxClearNewNotifications(request):
	global newNotificationList
	newNotificationList.clear()
	return HttpResponse()

def ajaxGetNotifications(request):
	global notificationList
	notificationList.reverse()
	wew = []
	for x in range(0, len(notificationList)):
		wew.append({"bedNumber":notificationList[x].bedNumber})
	notificationList.reverse()
	return JsonResponse(wew, safe=False)

def ajaxClearClicked(request):
	global buttonClicked
	buttonClicked.clear()
	return HttpResponse()

def	loginUsername (request): #ADDED
	global position

	username = request.GET.get('username')
	password = request.GET.get('password')

	n = Employee.objects.filter(username=username).exists()
	d = Doctor.objects.filter(username=username).exists()

	if n == True or d == True:
		print(n,d)
		if  Employee.objects.filter(username=username,password=password).exists() or Doctor.objects.filter(username=username,password=password).exists():
			if Employee.objects.filter(username=username,password=password).exists():
				e1 = Employee.objects.get(username=username,password=password)
				if e1.usertype == 'Nurse':
					position = 'Nurse'
					request.session['position'] = "NURSE"
				else:
					position = "Admin"
					request.session['position'] = "ADMIN"
			else:
				position = "Doctor"
				request.session['position'] = "DOCTOR"
			data = {
				'is_match': True,
				'position': position,
			}
	else:
		data = {
			'is_match': False
		}
	print(data)
	return JsonResponse(data)


#Nurse
def dashboard(request):

	session_position = request.session.get('position','none')
	if session_position == "NURSE":
		global notificationList
		global newNotificationList
		notificationList.reverse()
		what = []
		for x in range(0, len(notificationList)):
			what.append({"bedNumber":notificationList[x].bedNumber})
		notificationList.reverse()


		patients = Patient.objects.values('idPatient')
		wew = []
		for x in range(0,len(patients)):
			checkObj = HeartRate.objects.filter(idPatient_id  = patients[x]['idPatient']).select_related('idPatient').exists()
			checkObj2 = Temperature.objects.filter(idPatient_id = patients[x]['idPatient']).select_related('idPatient').exists()
			checkObj3 = Position.objects.filter(idPatient_id = patients[x]['idPatient']).select_related('idPatient').exists()
			if checkObj and checkObj2 and checkObj3:
				obj = HeartRate.objects.filter(idPatient_id = patients[x]['idPatient']).select_related('idPatient').latest('date','time')
				obj2 = Temperature.objects.filter(idPatient_id = patients[x]['idPatient']).select_related('idPatient').latest('date','time')
				obj3 = Position.objects.filter(idPatient_id = patients[x]['idPatient']).select_related('idPatient').latest('date','time')
				if obj.idPatient.status == "ON BED" or obj.idPatient.status == "STARTING":
					wew.append({"idPatient_id": patients[x]['idPatient'], "positionPatient":obj3.position.upper(),"firstName":obj.idPatient.firstName.upper(), "lastName":obj.idPatient.lastName.upper(),"heartRate":obj.heartRate,"temperature":obj2.temperature, "bedNumber":obj.idPatient.bedNumber.bedNumber,"minHeartRate":obj.idPatient.minHeartRate, "maxHeartRate":obj.idPatient.maxHeartRate, "minTemp":obj.idPatient.minTemp, "maxTemp":obj.idPatient.maxTemp, "patientStatus":obj.idPatient.status})

		context = {"patients_list": wew, 'position': request.session.get('position', 'none'), "notifications":what, "notificationSize":len(notificationList), "newNotificationList":len(newNotificationList)}
		return render(request, 'dashboard/dashboard.html',context)
	return render(request, 'blocked.html')
#Nurse AJAX
def ajaxUpdateDashboard(request):
	patients = Patient.objects.values('idPatient')
	wew = []
	ip = get_client_ip(request)
	print(ip)
	for x in range(0,len(patients)):
		checkObj = HeartRate.objects.filter(idPatient_id = patients[x]['idPatient']).select_related('idPatient').exists()
		checkObj2 = Temperature.objects.filter(idPatient_id = patients[x]['idPatient']).select_related('idPatient').exists()
		checkObj3 = Position.objects.filter(idPatient_id = patients[x]['idPatient']).select_related('idPatient').exists()
		if checkObj and checkObj2 and checkObj3:

			obj = HeartRate.objects.filter(idPatient_id = patients[x]['idPatient']).select_related('idPatient').latest('date','time')
			obj2 = Temperature.objects.filter(idPatient_id = patients[x]['idPatient']).select_related('idPatient').latest('date','time')
			obj3 = Position.objects.filter(idPatient_id = patients[x]['idPatient']).select_related('idPatient').latest('date','time')
			if obj.idPatient.status == "ON BED" or obj.idPatient.status == "STARTING":
				wew.append({"idPatient_id": patients[x]['idPatient'], "positionPatient":obj3.position.upper(),"firstName":obj.idPatient.firstName.upper(), "lastName":obj.idPatient.lastName.upper(),"heartRate":obj.heartRate,"temperature":obj2.temperature, "bedNumber":obj.idPatient.bedNumber.bedNumber, "minTemp":obj.idPatient.minTemp, "maxTemp":obj.idPatient.maxTemp, "maxHeartRate":obj.idPatient.maxHeartRate, "minHeartRate":obj.idPatient.minHeartRate, "patientStatus":obj.idPatient.status})

	return JsonResponse (wew, safe=False)


def get_client_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip


def	loginUsername (request): #ADDED
	global position

	username = request.GET.get('username')
	password = request.GET.get('password')

	n = Employee.objects.filter(username=username).exists()
	d = Doctor.objects.filter(username=username).exists()

	if n == True or d == True:
		print(n,d)
		if  Employee.objects.filter(username=username,password=password).exists() or Doctor.objects.filter(username=username,password=password).exists():
			if Employee.objects.filter(username=username,password=password).exists():
				e1 = Employee.objects.get(username=username,password=password)
				if e1.usertype == 'Nurse':
					position = 'Nurse'
					request.session['position'] = "NURSE"
				else:
					position = "Admin"
					request.session['position'] = "ADMIN"
			else:
				position = "Doctor"
				request.session['position'] = "DOCTOR"
				request.session['id'] = Doctor.objects.get(username=username).idDoctor
			data = {
				'is_match': True,
				'position': position,
			}
	else:
		data = {
			'is_match': False
		}
	print(data)
	return JsonResponse(data)



def loginChecker (request): ##FINALCHANGED
	global position

	initial = request.GET.get('initial') #ADDED
	initial = int(initial)
	r = RFID.objects.all().count()

	rfid = RFID.objects.latest('idRFID')
	rfid = rfid.RFIDnumber

	if initial == r:
		data = {
			'is.tapped': False
		}
	else:
		n = Employee.objects.filter(rfid=rfid).exists()
		d = Doctor.objects.filter(rfid=rfid).exists()
		print(n,d)
		#npass = Nurse.objects.filter(username=username).values('password')
		#dpass = Doctor.objects.filter(username=username).values('password')

		#print ("Nurse", npass)
		#print ("Doctor", dpass)
		if n == True:

			e1 = Employee.objects.get(rfid=rfid)

			if e1.usertype == 'Nurse':
				position = 'Nurse'
				request.session['position'] = "NURSE"
			else:
				position = "Admin"
				request.session['position'] = "ADMIN"
			data = {
				'is_match': True,
				'position': position,
			}
		elif d == True:

			position = "Doctor"
			request.session['position'] = "DOCTOR"
			request.session['id'] = Doctor.objects.get(rfid=rfid).idDoctor
			data = {
					'is_match': True,
					'position': position,
				}
		else:
			data = {
				'is_rfidexisting': False
			}


	return JsonResponse(data)




#Nurse
def managepatients(request):

	session_position = request.session.get('position','none')
	if session_position == "NURSE":
		global notificationList
		global newNotificationList
		notificationList.reverse()
		what = []
		for x in range(0, len(notificationList)):
			what.append({"bedNumber":notificationList[x].bedNumber})
		notificationList.reverse()


		patients_list = Patient.objects.all().select_related('bedNumber')

		beds_list = Beds.objects.filter(bedStatus = "Available")
		doctors_list = Doctor.objects.all()

		context = {'patients_list': patients_list,'beds_list': beds_list, 'doctors_list': doctors_list,"notifications":what, "notificationSize":len(notificationList), "newNotificationList":len(newNotificationList)}



		return render(request, 'dashboard/managepatients.html',context)
	return render(request, 'blocked.html')
# #Nurse
# def managebeds(request):
#
# 	session_position = request.session.get('position','none')
# 	if session_position == "NURSE":
# 		return render(request, 'dashboard/managebeds.html')
# 	return render(request, 'blocked.html')

#Nurse
def blocked(request):
	return render(request, 'blocked.html')

#Nurse
def reports(request):
	session_position = request.session.get('position','none')
	if session_position == "NURSE":
		return render(request, 'dashboard/reports.html')
	return render(request, 'blocked.html')
#Nurse
def viewpatients(request, idPatient):
	session_position = request.session.get('position','none')
	if session_position == "NURSE":
		p1 = Patient.objects.get(pk=idPatient)
		# doctors = Patient_Doctors.objects.filter(Patient_id = idPatient).select_related('Patient').select_related('Doctor')
		cursor = connection.cursor()
		cursor.execute("SELECT d.firstName, d.lastName, d.middleName FROM unodosmattress_Patient_Doctors pd JOIN unodosmattress_doctor d ON d.idDoctor = pd.Doctor_id WHERE pd.Patient_id = %s",[idPatient])
		doctors = cursor.fetchall()
		doctors_list = []
		for x in range(0, len(doctors)):
			doctors_list.append({"firstName":doctors[x][0], "lastName":doctors[x][1],"middleName":doctors[x][2]})

		context = {'patient':p1,'doctors':doctors_list}
		return render(request, 'dashboard/viewpatients.html',context)
	return render(request, 'blocked.html')
#Nurse AJAX
def ajaxDisplayDoctors(request):
	doctors = Doctor.objects.all()

	json_doctors = []

	for record in doctors:
		json_doctors.append({"idDoctor":record.idDoctor,"firstName":record.firstName})

	return JsonResponse (json_doctors, safe=False)

def getDoctorInfo(request):
	idDoctor = request.GET.get('idDoctor')
	doctor = Doctor.objects.get(pk=idDoctor)
	print(idDoctor	)
	json_doctors = []

	json_doctors.append({"idDoctor":doctor.idDoctor,"firstName":doctor.firstName, "lastName": doctor.lastName})

	return JsonResponse (json_doctors, safe=False)

def ajaxUpdateStatusPatient(request):
	id = request.GET.get('id')
	minTemp = request.GET.get('minTemp')
	maxTemp = request.GET.get('maxTemp')
	minHeartRate = request.GET.get('minHeartRate')
	maxHeartRate = request.GET.get('maxHeartRate')
	status = request.GET.get('status')
	p1 = Patient.objects.get(pk=id)
	p1.minTemp = minTemp
	p1.maxTemp = maxTemp
	p1.minHeartRate = minHeartRate
	p1.maxHeartRate = maxHeartRate
	if status == "ON BED":
		cursor = connection.cursor()
		cursor.execute(''' SET GLOBAL EVENT_SCHEDULER = ON ''')
		cursor.execute(''' CREATE EVENT event_updateStatus%s ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 3 MINUTE DO UPDATE unodosmattress_patient SET status = "ON BED" WHERE idPatient =  %s AND status = "STARTING" ''', [int(id), id])

		p1.status = "STARTING"
		body = "Your patient, " + str(p1.firstName) + " " + str(p1.lastName) + ", is now on the bed."
		now = datetime.datetime.now()
		date = now.date()
		time = now.time()
		news = News(body=body, date=date, time=time,idPatient_id=p1.pk)
		news.save()
	elif status == "FINISHED":
		p1.status = "FINISHED"
		body = "Your patient, " + str(p1.firstName) + " " + str(p1.lastName) + ", has been transferred to the ward."
		now = datetime.datetime.now()
		date = now.date()
		time = now.time()
		news = News(body=body, date=date, time=time,idPatient_id=p1.pk)
		news.save()
	p1.save()

	return HttpResponse()

#Nurse AJAX
def ajaxGetAvailableBeds(request):
	beds = Beds.objects.filter(bedStatus="Available")

	beds_array = []

	for record in beds:
		beds_array.append({"idBeds":record.idBeds,"bedNumber":record.bedNumber})

	return JsonResponse (beds_array, safe=False)

#Nurse AJAX
def ajaxAddPatient(request):
	firstName = request.GET.get('firstName')
	middleName = request.GET.get('middleName')
	lastName = request.GET.get('lastName')
	birthDate = request.GET.get('birthDate')
	religion = request.GET.get('religion')
	minTemp = request.GET.get('minTemp')
	maxTemp = request.GET.get('maxTemp')
	minHeartRate = request.GET.get('minHeartRate')
	maxHeartRate = request.GET.get('maxHeartRate')
	contactperson = request.GET.get('contactperson')
	contactNum = request.GET.get('contactNum')
	bedNumber = request.GET.get('bedNumber')
	bday = parse_date(birthDate)
	# age = (datetime.now().date() - bday).days / 365.25
	print(bday)
	doctors = request.GET.getlist('doctors[]')

	patient_var = Patient(firstName = firstName, middleName = middleName, lastName = lastName, birthDate = birthDate, religion = religion, minTemp = minTemp, maxTemp = maxTemp, minHeartRate = minHeartRate, maxHeartRate = maxHeartRate,contactperson=contactperson, contactNum = contactNum, bedNumber_id = int(bedNumber), status = "RESERVED")
	patient_var.save()

	patient_bed = Patient_Table(idBeds_id=bedNumber, idPatient_id=patient_var.pk)
	patient_bed.save()

	client = coreapi.Client()
	schema = client.get("http://192.168.100.214:8000/docs")
	action = ["patient","create"]
	params = {
		"idPatient": patient_var.pk
	}
	result = client.action(schema, action, params=params)

	for x in range(0, len(doctors)):
		patient_doctor = Patient_Doctors( Doctor_id = doctors[x], Patient_id = patient_var.pk)
		patient_doctor.save()
	body = "Your patient, " + str(patient_var.firstName) + " " + str(patient_var.lastName) + ", is now in the recovery room."
	now = datetime.datetime.now()
	date = now.date()
	time = now.time()
	news = News(body=body, date=date, time=time, idPatient_id= patient_var.pk)
	news.save()
	bed = Beds.objects.get(pk = bedNumber)
	bed.bedStatus = "Occupied"
	bed.save()
	return HttpResponse()

def ajaxGetPatients(request):

	patients = Patient.objects.all()
	patients_array = []

	for record in patients:
		patients_array.append({"idPatient":record.idPatient,"firstName":record.firstName,"lastName":record.lastName,
		"middleName":record.middleName,"bedNumber":record.bedNumber.bedNumber,"status":record.status})
	print(patients_array)
	return JsonResponse(patients_array, safe=False)

#---------------------API -------------------------------------
class TemperatureList(generics.ListCreateAPIView):
	queryset = Temperature.objects.all()
	serializer_class = TemperatureSerializer

class TemperatureDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Temperature.objects.all()
	serializer_class = TemperatureSerializer

class HeartRateList(generics.ListCreateAPIView):
	queryset = HeartRate.objects.all()
	serializer_class = HeartRateSerializer

class HeartRateDetail(generics.RetrieveUpdateDestroyAPIView):

	queryset = HeartRate.objects.all()
	serializer_class = HeartRateSerializer

class TemperatureEveryMinList(generics.ListCreateAPIView):
	queryset = TemperatureEveryMinute.objects.all()
	serializer_class = TemperatureEveryMinSerializer

class TemperatureEveryMinDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = TemperatureEveryMinute.objects.all()
	serializer_class = TemperatureEveryMinSerializer

class HeartRateEveryMinList(generics.ListCreateAPIView):
	queryset = HeartRateEveryMinute.objects.all()
	serializer_class = HeartRateEveryMinSerializer

class HeartRateEveryMinDetail(generics.RetrieveUpdateDestroyAPIView):

	queryset = HeartRateEveryMinute.objects.all()
	serializer_class = HeartRateEveryMinSerializer



class BedList(generics.ListCreateAPIView):
	queryset = Beds.objects.all()
	serializer_class = BedSerializer

class BedDetail(generics.RetrieveUpdateDestroyAPIView):

	queryset = Beds.objects.all()
	serializer_class = BedSerializer

class RFIDList(generics.ListCreateAPIView):
	queryset = RFID.objects.all()
	serializer_class = RFIDSerializer

class RFIDDetail(generics.RetrieveUpdateDestroyAPIView):

	queryset = RFID.objects.all()
	serializer_class = RFIDSerializer

class PositionList(generics.ListCreateAPIView):
	queryset = Position.objects.all()
	serializer_class = PositionSerializer

class PositionDetail(generics.RetrieveUpdateDestroyAPIView):

	queryset = Position.objects.all()
	serializer_class = PositionSerializer


# class NotificationList(generics.ListCreateAPIView):
# 	queryset = Notification.objects.all()
# 	serializer_class = NotificationSerializer
#
# class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):
# 	serializer_class = NotificationSerializer


#-------------------ADMIN ------------------------------
def manageusers(request):
	d1 = Doctor.objects.all()
	e1 = Employee.objects.all()
	r = RFID.objects.all().count()
	users = []
	count = []

	count.append({"r":r})
	for x in range(0,len(d1)):

		users.append({'id':d1[x].pk, "username":d1[x].username,"firstName":d1[x].firstName, "middleName":d1[x].middleName, "lastName":d1[x].lastName, "userType":"Doctor"})

	for z in range(0, len(e1)):
		users.append({'id':e1[z].pk, "username":e1[z].username,"firstName":e1[z].firstName, "middleName":e1[z].middleName, "lastName":e1[z].lastName, "userType":e1[z].usertype})
	context = {"users_list": users, "rfid_count": count}
	return render(request, 'admin/manageusers.html', context)

def managebeds(request):
	beds_list = Beds.objects.filter(bedStatus="Pending")
	availableBeds = Beds.objects.filter(bedStatus="Available")
	unavailableBeds = Beds.objects.filter(bedStatus="Unavailable")

	occupiedBeds = Beds.objects.filter(bedStatus="Occupied")

	context = {'beds_list': beds_list,'availableBeds':availableBeds, 'unavailableBeds':unavailableBeds, 'occupiedBeds':occupiedBeds, 'availableBedsSize': len(availableBeds), 'unavailableBedsSize':len(unavailableBeds), 'occupiedBedsSize':len(occupiedBeds)}

	return render(request, 'admin/managebeds.html',context)

def reports(request):
	return render(request, 'dashboard/reports.html')

def viewusers(request, username):
	d1 = Doctor.objects.filter(username=username).exists()
	e1 = Employee.objects.filter(username=username).exists()
	context = {}
	if d1 == True:
		doctor = Doctor.objects.get(username=username)
		context = {'user': doctor, 'usertype':'Doctor'}
	elif e1 == True:
		employee = Employee.objects.get(username=username)
		context = {'user': employee,'usertype':employee.usertype}
	return render(request, 'admin/viewusers.html', context)

def home(request):
	p = Employee.objects.filter(usertype="Nurse")
	nurseSize = len(p)
	d = Doctor.objects.all()
	doctorSize = len(d)

	availableBeds = Beds.objects.filter(bedStatus="Available")
	unavailableBeds = Beds.objects.filter(bedStatus="Unavailable")
	occupied = Beds.objects.filter(bedStatus="Occupied")

	context = {"nurseSize":nurseSize, "doctorSize":doctorSize, "availableBeds":len(availableBeds), "unavailableBeds":len(unavailableBeds),"occupiedBeds":len(occupied)}
	return render(request, 'admin/home.html',context)

def login(request):
	r = RFID.objects.all().count()
	count = []

	count.append({"r":r})
	context = {"rfid_count": count}
	return render(request, 'login.html',context)

def ajaxrfidCount(request):

	initial = request.GET.get('initial')
	initial = int(initial)
	r = RFID.objects.all().count()
#	latest = RFID.objects.get(idRFID=initial)

#	print(latest)

	if initial == r:
		data = {
			'newID': False
		}
	else:
		#IT MEANS MAY NEW ID NA
		data = {
			'newID': True
		}

	return JsonResponse (data, safe=False)

def logout(request): ##CHANGED
	print("CLEAR SESSION")


	r = RFID.objects.all().count()
	count = []

	count.append({"r":r})
	context = {"rfid_count": count}
	return render(request, 'login.html',context)

def ajaxSetBedAvailable(request):

	idBed = request.GET.get('id')
	bedNumber = request.GET.get('bedNumber')
	b1 = Beds.objects.get(idBeds = idBed)
	b1.bedStatus = "Available"
	b1.bedNumber = bedNumber
	b1.save()
	client = coreapi.Client()
	schema = client.get("http://192.168.100.214:8000/docs")
	action = ["bed","create"]
	params = {
		"bedNumber": bedNumber
	}
	result = client.action(schema, action, params=params)

	return HttpResponse()

def ajaxUpdateBedStatus(request):
	aList = request.GET.getlist('aList[]')
	uList = request.GET.getlist('uList[]')
	print(aList)
	for x in range(0, len(aList)):
		key =int(float(aList[x]))
		temp = Beds.objects.get(pk=key)
		temp.bedStatus = "Available"
		temp.save()
	for w in range(0, len(uList)):
		key = int(float(uList[w]))
		temp = Beds.objects.get(pk=key)
		temp.bedStatus = "Unavailable"
		temp.save()

	return HttpResponse()

def ajaxGetPendingBeds(request):

	beds = Beds.objects.filter(bedStatus="Pending")

	beds_array = []

	for record in beds:
		beds_array.append({"idBeds":record.idBeds,"bedNumber":record.bedNumber, "bedStatus":record.bedStatus})

	return JsonResponse (beds_array, safe=False)

def ajaxRefreshAvailableBeds(request):

	beds = Beds.objects.filter(bedStatus="Available")

	beds_array = []

	for record in beds:
		beds_array.append({"idBeds":record.idBeds,"bedNumber":record.bedNumber, "bedStatus":record.bedStatus})

	return JsonResponse (beds_array, safe=False)

def ajaxRefreshUnavailableBeds(request):

	beds = Beds.objects.filter(bedStatus="Unavailable")

	beds_array = []

	for record in beds:
		beds_array.append({"idBeds":record.idBeds,"bedNumber":record.bedNumber, "bedStatus":record.bedStatus})

	return JsonResponse (beds_array, safe=False)



def ajaxCheckUser(request):

	#nurses= Nurse.objects.all()
	#doctors= Doctor.objects.all()

	#users = []

	#for user in nurses:
	#	users.append({"username": user.username})

	#for user in doctors:
	#	users.append({"username": user.username})

	#print(users)

	userType = request.GET.get('userType')
	print("userType", " ", userType)
	firstName = request.GET.get('firstName')
	middleName = request.GET.get('middleName')
	lastName = request.GET.get('lastName')
	contactNum = request.GET.get('contactNum')
	username = request.GET.get('username')
	password = request.GET.get('password')
	password2 = request.GET.get('password2')
	initial = request.GET.get('initial') #ADDED

	r = RFID.objects.all().count()

	rfid = RFID.objects.latest('idRFID')
	rfid = rfid.RFIDnumber
	print(rfid)

	n = Employee.objects.filter(rfid=rfid).exists()
	d = Doctor.objects.filter(rfid=rfid).exists()

	print ("N", n)
	print ("D", d)

	if n == True or d == True:
		data = {
			'is_existing': True
		}

	else:
		data = {
				'is_existing': False
			}

	print(data)
	if userType == "Nurse" or userType == "Admin" and n == False:
		print("HI")
		if initial == r:
			data = {
				'is_newrfid': False
			}

		else:
			data = {
				'is_newrfid': True
			}
			if password != password2:
				data = {
					'is_match': False
				}
			else:
				data = {
					'is_match': True
				}
				if 	Doctor.objects.filter(rfid=rfid).exists() or Employee.objects.filter(rfid=rfid).exists():
					data = {
						'is_rfidexisting': True
					}
				else:
					data = {
						'is_rfidexisting': False
					}
					print("TAPPED YUNG COUNT")
					emp_var = Employee(firstName = firstName, middleName = middleName, lastName = lastName, contactNum = contactNum, username = username, password = password,usertype = userType,rfid = rfid)
					emp_var.save()
					print("YES SAVED NURSE WITH RFID")


	elif userType == "Doctor" and d == False:
		print("HII")
		if initial == r:
			data = {
				'is_newrfid': False
			}

		else:
			data = {
				'is_newrfid': True
			}
			if password != password2:
				data = {
					'is_match': False
				}
			else:
				if Doctor.objects.filter(rfid=rfid).exists() or Employee.objects.filter(rfid=rfid).exists():
					data = {
						'is_rfidexisting': True
					}
				else:
					data = {
						'is_rfidexisting': False
					}
					doctor_var = Doctor(firstName = firstName, middleName = middleName, lastName = lastName, contactNum = contactNum, username = username, password = password,rfid = rfid)
					doctor_var.save()
					print("YES SAVED DOCTOR WITH RFID")
					data = {
							'is_match': True
					}


	return JsonResponse(data)

def ajaxSaveNewPassword(request):
	id = request.GET.get('id')
	position = request.GET.get('position')
	password = request.GET.get('password')

	if position == "Doctor":
		u1 = Doctor.objects.get(pk=id)

	elif position == "Nurse" or position == "Admin":
		u1 = Employee.objects.get(pk = id)

	u1.password = password
	u1.save()


	return HttpResponse()

#---------------DOCTOR --------------------------
def patients(request):
	idDoctor = request.session.get('id','none')
	cursor = connection.cursor()
	cursor.execute("SELECT p.idPatient, p.lastName, p.firstName, p.middleName, p.status FROM unodosmattress_patient p JOIN unodosmattress_Patient_Doctors pd ON pd.Patient_id = p.idPatient WHERE pd.Doctor_id = %s",[idDoctor])
	wew = cursor.fetchall()
	patients = []
	for x in range(0,len(wew)):
		patients.append({"idPatient":wew[x][0], "lastName":wew[x][1], "firstName":wew[x][2], "middleName":wew[x][3], "status":wew[x][4]})
	context = {"patients_list":patients}
	return render(request, 'doctor/patients.html',context)

def mypatients(request):
	idDoctor = request.session.get('id','none')
	cursor = connection.cursor()
	cursor.execute("SELECT p.idPatient, p.lastName, p.firstName, p.middleName, p.status FROM unodosmattress_patient p JOIN unodosmattress_Patient_Doctors pd ON pd.Patient_id = p.idPatient WHERE pd.Doctor_id = %s",[idDoctor])
	wew = cursor.fetchall()
	patients = []
	for x in range(0,len(wew)):
		patients.append({"idPatient":wew[x][0], "lastName":wew[x][1], "firstName":wew[x][2], "middleName":wew[x][3], "status":wew[x][4]})
	context = {"patients_list":patients}
	return render(request, 'doctor/mypatients.html', context)

def view(request, pk):
	patient = Patient.objects.get(pk = pk)
	cursor = connection.cursor()
	cursor.execute("SELECT d.firstName, d.lastName, d.middleName FROM unodosmattress_Patient_Doctors pd JOIN unodosmattress_doctor d ON d.idDoctor = pd.Doctor_id WHERE pd.Patient_id = %s",[pk])
	doctors = cursor.fetchall()
	doctors_list = []
	for x in range(0, len(doctors)):
		doctors_list.append({"firstName":doctors[x][0], "lastName":doctors[x][1],"middleName":doctors[x][2]})
	context = {"patient":patient, "doctors_list": doctors_list}
	return render(request, 'doctor/view.html', context)

def reports(request,pk):
	p1 = Patient.objects.get(pk=pk)

	h = HeartRateEveryMinute.objects.filter(idPatient_id=pk)

	t = TemperatureEveryMinute.objects.filter(idPatient_id =pk)

	heartRateList = []
	for x in range(0, len(h)):
		heartRateList.append({"idHeartRate":h[x].idHeartRate, "heartRate":h[x].heartRate,"time":h[x].time, "date":h[x].date},)
	temperatureList = []
	for q in range(0, len(t)):
		temperatureList.append({"idTemperature":t[q].idTemperature, "temperature":t[q].temperature, "time":t[q].time,"date":t[q].date})

	cursor = connection.cursor()
	cursor.execute("SELECT * FROM (select HOUR(TIME) AS 'hour', POSITION, COUNT(POSITION) as 'count' FROM unodosmattress_position where idPatient_id = %s group by HOUR(TIME), POSITION ORDER BY hour(time), count desc) X GROUP BY hour", [pk])
	fetch = cursor.fetchall()
	positionList = []

	for w in range(0, len(fetch)):
		positionList.append({"hour":fetch[w][0], "position":fetch[w][1].upper(), "count":fetch[w][2]})
	context = {"patient":p1, "heartRateList":heartRateList,"temperatureList":temperatureList, "positionList":positionList, "firstName":p1.firstName, "lastName":p1.lastName, "minHeartRate":p1.minHeartRate, "maxHeartRate":p1.maxHeartRate}

	return render(request, 'doctor/reports.html',context)

def ajaxGetEveryMinHeartRate(request):

	idPatient = request.GET.get('idPatient')
	h = HeartRateEveryMinute.objects.filter(idPatient_id=idPatient)

	heartRateList = []
	for x in range(0, len(h)):
		heartRateList.append({"idHeartRate":h[x].idHeartRate, "heartRate":h[x].heartRate,"time":h[x].time, "date":h[x].date})

	t = TemperatureEveryMinute.objects.filter(idPatient_id = idPatient)
	temperatureList = []
	for q in range(0, len(t)):
		temperatureList.append({"idTemperature":t[q].idTemperature, "temperature":t[q].temperature, "time":t[q].time,"date":t[q].date})

	data = {"heartRateList":heartRateList, "temperatureList":temperatureList}

	return JsonResponse(data, safe=False)


def doctorhome(request):
	idDoctor = request.session.get('id','none')
	size = Patient_Doctors.objects.filter(Doctor_id=idDoctor)
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM unodosmattress_Patient_Doctors PD JOIN unodosmattress_patient P ON P.idPatient = PD.Patient_id WHERE PD.DOCTOR_ID = %s AND P.status = 'FINISHED'", [idDoctor])
	stableSize = cursor.fetchall()
	cursor.execute("SELECT * FROM unodosmattress_Patient_Doctors PD JOIN unodosmattress_patient P ON P.idPatient = PD.Patient_id WHERE PD.DOCTOR_ID = %s AND P.status = 'ON BED'", [idDoctor])
	onBedSize = cursor.fetchall()
	doctor = Doctor.objects.get(pk=idDoctor)

	cursor.execute("SELECT n.idNews, n.body, n.date, n.time FROM unodosmattress_news n JOIN unodosmattress_patient p on p.idPatient = n.idPatient_id JOIN unodosmattress_patient_doctors pd ON pd.Patient_id = p.idPatient WHERE pd.Doctor_id = %s", [idDoctor])
	wew = cursor.fetchall()
	list = []
	for x in range(0, len(wew)):
		date = wew[x][2]
		list.append({"idNews":wew[x][0],"body":wew[x][1],"date":wew[x][2],"time":wew[x][3],"year":date.strftime("%Y"), "month":date.strftime("%B"),"day":date.strftime("%d")})


	context = {"size":len(size), "stableSize":len(stableSize), "doctor":doctor, "onBedSize":len(onBedSize),"newsList":list}


	return render(request, 'doctor/home.html',context)
