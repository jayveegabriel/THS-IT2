import serial
import time
import threading


class SIM800 :

    def __init__ (self, port, speed):
        self.ser=serial.Serial(port, speed)
        self.buffer_end=0
        self.sms_buffer={}

    def gsmReset (self):
        self.ser.write('ATZ\r'.encode())
        time.sleep(0.5)
        reply=self.ser.read(self.ser.inWaiting()).decode()
        #print (result)
        if ('OK' in reply):
            return 1
        else :
            return -1 

    def smsInit (self):
        self.ser.write('AT+CMGF=1\r'.encode())
        time.sleep(0.5)
        reply=self.ser.read(self.ser.inWaiting()).decode()
        #print (result)
        if ('OK' in reply):
            return 1
        else :
            return -1

    def smsSend (self, phone_number, message):
        self.ser.write(('AT+CMGS="'+str(phone_number)+'"\r').encode())
        time.sleep(2)
        self.ser.write((str(message) + '\x1A\r').encode())
        #self.ser.write('\x1A\r'.encode())
        return 0

    def clear_buffer (self):
        self.ser.read(self.ser.inWaiting()).decode()
        return 0

    def smsDelete_All (self):
        self.ser.write('AT+CMGDA="DEL ALL"\r'.encode())
        time.sleep(0.5)
        reply=self.ser.read(self.ser.inWaiting())
        return 0

    def smsRead (self, index):
        command='AT+CMGR='+str(index)+'\r'
        self.ser.write(command.encode())
        time.sleep(0.5)
        buffer=self.ser.read(self.ser.inWaiting()).decode()
        if ("UNREAD" in buffer):
            nCtr = 0
            msgcount = 0
            for line in buffer.split('\r'):
                nCtr += 1
                if "+CMGR:" in line:
                    msgcount = nCtr
                    number = line.split(',')[1][1:-1]
                    date = line.split(',')[3][1:] + " " + line.split(',')[4][:-1]
            message = buffer.split('\r')[msgcount][1:]
            sms={"status":1,"date":date, "phone":number, "message":message}
        else:
            sms={"status":0}
        return sms

    def smsReader(self):
        while True:
            buffer=self.smsRead(1)
    
            if (buffer['status']==1):
                sms_buffer.append(buffer)
                self.smsDelete(1)
            time.sleep(0.5)
        
        return 0

    def smsThreadRead(self):
        try:
            thread.start_new_thread(smsReader, "wReader")
        except:
            print ("Error: Unable to start thread")

        while 1:
            pass
        return 0

    def smsRead_all (self):
        self.ser.write('AT+CMGL="ALL"\r'.encode())
        time.sleep(0.5)
        buffer=self.ser.read(self.ser.inWaiting()).decode()
        print (buffer)

        return 0

    def smsUnread (self):
        self.ser.write('AT+CMGL="REC UNREAD"\r'.encode())
        time.sleep(0.5)
        buffer=self.ser.read(self.ser.inWaiting()).decode()
        print (buffer)

        return 0

    def smsDelete (self, index):
        command='AT+CMGD='+str(index)+'\r'
        self.ser.write(command.encode())
        time.sleep(0.5)
        buffer=self.ser.read(self.ser.inWaiting()).decode()

        return 0




        
