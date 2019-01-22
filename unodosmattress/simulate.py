import coreapi
import threading



def sendData():
  threading.Timer(1.0, sendData).start()
  client = coreapi.Client()
  tempSchema = client.get("http://192.168.100.222:8000/docs")
  tempAction = ['temperature','create']
  tempParams = {
    "temperature":33.1,
    "date": "2018-10-10",
    "time": "23:59:59"
  }
  hrResult = client.action(tempSchema, tempAction, params = tempParams)

  hrAction = ['heartrate','create']
  hrParams = {
    "heartRate": 73,
    "date": "2018-10-10",
    "time": "23:59:59"
  }

  hrResult = client.action(tempSchema, hrAction, params = hrParams)


  posAction = ['position','create']
  posParams = {
    "position": "back",
    "date": "2018-10-10",
    "time": "23:59:59",
  }
  # posResult = client.action(tempSchema, posAction, params =posParams)

sendData()