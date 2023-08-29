import paho.mqtt.client as paho
import sys
client= paho.Client()
if client.connect("localhost",1883,60) != 0:  # server address
	print("Could not connect to MQTT Broker")
	sys.exit(-1)
client.publish("test/status", "Hi",0)
client.disconnect()
