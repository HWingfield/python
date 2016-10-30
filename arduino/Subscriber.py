from mosquitto import *
from serial import *
from random import *

arduino = Serial("COM1",9600,timeout=2)

clientfind = Mosquitto("HARRISON")
clientfind.connect("10.212.61.136")

clientfind.subscribe("/lights")

def messageReceived(broker, obj, msg):
    payload = msg.payload.decode()
    print("Message " + msg.topic + " containing: " + payload)
    
    if (payload == "ON"):
        message = "1"
    if (payload == "OFF"):
        message = "0"
    arduino.write(message.encode())    

clientfind.on_message = messageReceived

while (client != None): client.loop()
