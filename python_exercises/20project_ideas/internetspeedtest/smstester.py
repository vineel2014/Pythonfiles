
"""
Python program to send sms with GSM SIM and GSM USB Modem
"""
import serial
import time

class TextMessage:
    def __init__(self, recipient="<--Recipient Details-->", message="Message"):
        self.recipient = recipient
        self.content = message

    def setRecipient(self, number):
        self.recipient = number
        print("Recipient Selection Done")

    def setContent(self, message):
        self.content = message
        print("Message Selected")

    def connectPhone(self):
        self.ser = serial.Serial('/dev/ttyUSB0', 460800, timeout=5)
        time.sleep(1)
        print("Phone Connected")

    def sendMessage(self):
        self.ser.write('ATZ\r')
        time.sleep(1)
        self.ser.write('AT+CMGF=1\r')
        time.sleep(1)
        self.ser.write('''AT+CMGS="''' + self.recipient + '''"\r''')
        time.sleep(1)
        self.ser.write(self.content + "\r")
        time.sleep(1)
        self.ser.write(chr(26))
        time.sleep(1)
        print("Message Sent")

    def disconnectPhone(self):
        self.ser.close()
        print("Phone Disconnected")

t=TextMessage()
t.connectPhone()
t.setContent("<--Message to send-->")

l=["<--List of Recipients-->"]

for i in l:
    t.setRecipient(i)
    t.sendMessage()

t.disconnectPhone()


