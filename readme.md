## Windows Application
```cmd
winget install -e --id EclipseFoundation.Mosquitto
```

1. ## MQTT Broker

	mosquitto -v

2. ## MQTT Subscriber

	mosquitto_sub -t test/status
 or  python3 mqtt_pub.py
3. ## MQTT Publisher
 python3 mqtt_pub.py
