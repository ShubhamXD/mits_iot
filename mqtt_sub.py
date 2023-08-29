import paho.mqtt.client as paho
import sys
def onMessage(client,userdata,msg):
	print(msg.topic + " :  "+ msg.payload.decode())
	
client= paho.Client()
client.on_message= onMessage
if client.connect("localhost",1883,60) != 0:  # server address
	print("Could not connect to MQTT Broker")
	sys.exit(-1)
client.subscribe("test/status")
try:
	client.loop_forever()
except:
	client.disconnect()
