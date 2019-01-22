import serial
import coreapi
import time

arduino = serial.Serial('COM4', 9600, timeout=.1)

store = ""
value = ""

store = arduino.readline()
while(True):
	time.sleep(1)
	store = arduino.readline()
	## print(store)
	value = store.decode('utf-8')
	print("ID:" + value)

	if value != "":
		print("HI")

		client = coreapi.Client()
		schema = client.get("http://192.168.100.222:8000/docs")
		action = ["rfid","create"]
		params = {
		 		"RFIDnumber": value,
		}
		result = client.action(schema,action,params=params)
		print("EW")


 