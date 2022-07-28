from distutils.command.clean import clean
import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Temperature_Outside")
client.connect(mqttBroker)

while True:
    randomNumber = randrange(0.0,10.0)
    client.publish("Temperature",randomNumber)
    print("Just published",str(randomNumber),"to topic Temperatrue")
    time.sleep(2)