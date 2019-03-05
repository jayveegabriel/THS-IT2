from rest_framework import serializers
from django.db import connection
from unodosmattress.models import *
import coreapi
from unodosmattress import sim800

class TemperatureSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Temperature
		fields = ('url', 'idTemperature', 'temperature','date','time','idPatient_id')
		extra_kwargs = {
            'url': {
                'view_name': 'unodosmattress:temperature-detail',
           	}
	}
	def create(self, validated_data):
		#CALL API TO GET THE CURRENT PATIENT


		tempTime = validated_data.get('time','')

		now = datetime.datetime.now()
		date = str(now.strftime("%Y-%m-%d"))
		time = str(now.strftime("%H:%M:%S"))

		if str(tempTime) == "23:59:59":

			todo = Temperature(
	        	temperature= validated_data.get('temperature', ''),
	        	date=date,
	        	time=time,
				idPatient_id = 10,
				)
			todo.save()

		else:

			client = coreapi.Client()
			schema = client.get("http://192.168.100.214:8000/docs")
			action = ["patient","list"]
			result = client.action(schema,action)
			patient = result[0]['idPatient']

			todo = Temperature(
	        	temperature= validated_data.get('temperature', ''),
	        	date=validated_data.get('date', ''),
	        	time=validated_data.get('time', ''),
				idPatient_id = patient,
				)
			todo.save()
		
			#return todo
		return todo

class PositionSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Position
		fields = ('url', 'idPosition', 'position','date','time','idPatient_id')
		extra_kwargs = {
            'url': {
                'view_name': 'unodosmattress:position-detail',
           	}
	}
	def create(self, validated_data):
		#CALL API TO GET THE CURRENT PATIENT
		# client = coreapi.Client()
		# schema = client.get("http://192.168.100.214:8000/docs")
		# action = ["patient","list"]
		# result = client.action(schema,action)
		# patient = result[0]['idPatient']

		now = datetime.datetime.now()
		date = str(now.strftime("%Y-%m-%d"))
		time = str(now.strftime("%H:%M:%S"))


		tempTime = validated_data.get('time','')


		if str(tempTime) == "23:59:59":
			todo = Position(
	        	position= (validated_data.get('position', '')).upper(),
	        	date=date,
	        	time=time,
				idPatient_id = 10,
				)
			todo.save()

			# return todo
		else:
			client = coreapi.Client()
			schema = client.get("http://192.168.100.214:8000/docs")
			action = ["patient","list"]
			result = client.action(schema, action)
			if result:
				patient = result[0]['idPatient']
				todo = Position(
		        	position = (validated_data.get('position', '')).upper(),
		        	date=date,
		        	time=time,
					idPatient_id = patient,
					)
				todo.save()
			else:
				todo = Position(
	        	position= (validated_data.get('position', '')).upper(),
	        	date=date,
	        	time=time,
				idPatient_id = 10,
				)
				todo.save()
		
		return todo

class HeartRateSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = HeartRate
		fields = ('url', 'idHeartRate', 'heartRate','date','time','idPatient_id')
		extra_kwargs = {
            'url': {
                'view_name': 'unodosmattress:heartRate-detail',
           	}
		}
	def create(self, validated_data):
		#CALL API TO GET THE CURRENT PATIENT

		now = datetime.datetime.now()
		date = str(now.strftime("%Y-%m-%d"))
		time = str(now.strftime("%H:%M:%S"))


		tempTime = validated_data.get('time','')


		if str(tempTime) == "23:59:59":
			hr = HeartRate(
	        	heartRate=validated_data.get('heartRate', ''),
	        	date=date,
	        	time=time,
				idPatient_id = 10,
			)
			hr.save()

		
			# return hr
		else:
			client = coreapi.Client()
			schema = client.get("http://192.168.100.214:8000/docs")
			action = ["patient","list"]
			result = client.action(schema, action)
			patient = result[0]['idPatient']
			if patient:
				hr = HeartRate(
			    	heartRate=validated_data.get('heartRate', ''),
			    	date=validated_data.get('date', ''),
			    	time=validated_data.get('time', ''),
					idPatient_id = patient,
				)
				hr.save()
			else:
				hr = HeartRate(
	        	heartRate=validated_data.get('heartRate', ''),
	        	date=date,
	        	time=time,
				idPatient_id = 10,
				)
				hr.save()
		return hr

class TemperatureEveryMinSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = TemperatureEveryMinute
		fields = ('url', 'idTemperature', 'temperature','date','time','idPatient_id')
		extra_kwargs = {
            'url': {
                'view_name': 'unodosmattress:temperature-detail',
           	}
	}
	def create(self, validated_data):
		#CALL API TO GET THE CURRENT PATIENT



		now = datetime.datetime.now()
		date = str(now.strftime("%Y-%m-%d"))
		time = str(now.strftime("%H:%M:%S"))


		tempTime = validated_data.get('time','')


		if str(tempTime) == "23:59:59":
			todo = TemperatureEveryMinute(
	        	temperature= validated_data.get('temperature', ''),
	        	date=date,
	        	time=time,
				idPatient_id = 10,
				)
			todo.save()
			# return todo
		else:
			client = coreapi.Client()
			schema = client.get("http://192.168.100.214:8000/docs")
			action = ["patient","list"]
			result = client.action(schema,action)
			patient = result[0]['idPatient']
			todo = TemperatureEveryMinute(
	        	temperature= validated_data.get('temperature', ''),
	        	date=validated_data.get('date', ''),
	        	time=validated_data.get('time', ''),
				idPatient_id = patient,
				)
			todo.save()
		return todo

class HeartRateEveryMinSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = HeartRateEveryMinute
		fields = ('url', 'idHeartRate', 'heartRate','date','time','idPatient_id')
		extra_kwargs = {
            'url': {
                'view_name': 'unodosmattress:heartRate-detail',
           	}
		}
	def create(self, validated_data):
		#CALL API TO GET THE CURRENT PATIENT


		now = datetime.datetime.now()
		date = str(now.strftime("%Y-%m-%d"))
		time = str(now.strftime("%H:%M:%S"))


		tempTime = validated_data.get('time','')


		if str(tempTime) == "23:59:59":
			hr = HeartRateEveryMinute(
	        	heartRate=validated_data.get('heartRate', ''),
	        	date=date,
	        	time=time,
				idPatient_id = 10,
			)
			hr.save()
			# return hr

		else:

			client = coreapi.Client()
			schema = client.get("http://192.168.100.214:8000/docs")
			action = ["patient","list"]
			result = client.action(schema, action)
			patient = result[0]['idPatient']
			hr = HeartRateEveryMinute(
	        	heartRate=validated_data.get('heartRate', ''),
	        	date=validated_data.get('date', ''),
	        	time=validated_data.get('time', ''),
				idPatient_id = patient,
			)
			hr.save()
		return hr


class RFIDSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = RFID
		fields = ('url', 'idRFID', 'RFIDnumber')
		extra_kwargs = {
            'url': {
                'view_name': 'unodosmattress:rfid-detail',
           	}
	}
	def create(self, validated_data):
		hr = RFID(
        	RFIDnumber=validated_data.get('RFIDnumber', ''),
        	)
		hr.save()

		return hr

# class NotificationSerializer(serializers.HyperlinkedModelSerializer):
#
# 	class Meta:
# 		model = Notification
# 		fields = ('url', 'idBeds')
# 		extra_kwargs = {
#             'url': {
#                 'view_name': 'unodosmattress:notification-detail'
#            	}
# 	}
# 	def create(self, validated_data):
# 		n = Notification(
#         	idBeds=validated_data.get('idBeds', ''),
#         	)
# 		n.save()
# 		return n




class BedSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Beds
		fields = ('url','bedNumber','bedStatus')
		extra_kwargs = {
			'url':{
				'view_name': 'unodosmattress:bed-detail'
			}
		}

	def create(self, validated_data):
		beds = Beds.objects.all()
		i = 1
		isOkay = False
		bedNumber = 0
		while isOkay == False:
			wew = 0
			for x in range(0, len(beds)):

				if(beds[x].bedNumber == i):
					wew = 1
			if wew == 0:
				bedNumber = i
				isOkay = True
			i = i + 1


		bed = Beds(
        	bedNumber= bedNumber,
        	bedStatus='Pending',
        	)
		bed.save()


		cursor = connection.cursor()

		cursor.execute(''' SET GLOBAL EVENT_SCHEDULER = ON''');
		cursor.execute('''DROP EVENT if exists event_removeBeds ''');
		cursor.execute('''CREATE EVENT event_removeBeds%s
						ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 30 SECOND
						DO
		UPDATE unodosmattress_beds SET bedStatus = "Expired" WHERE idBeds =  %s AND bedStatus = "Pending" ''',[bed.pk,bed.pk])
		return bed
