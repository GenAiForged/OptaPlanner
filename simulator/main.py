import paho.mqtt.client as mqtt
import time
import json
import random

# MQTT Broker settings
BROKER_ADDRESS = "mqtt_broker"
BROKER_PORT = 1883
TOPIC = "telemetry"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print(f"Failed to connect, return code {rc}\n")

def on_publish(client, userdata, mid):
    print(f"Message {mid} published.")

client = mqtt.Client(client_id="simulator")
client.on_connect = on_connect
client.on_publish = on_publish
client.connect(BROKER_ADDRESS, BROKER_PORT)

client.loop_start()

try:
    while True:
        temperature = random.uniform(20.0, 30.0)
        pressure = random.uniform(1.0, 1.5)
        payload = {"temperature": temperature, "pressure": pressure}
        client.publish(TOPIC, json.dumps(payload))
        print(f"Published: {payload}")
        time.sleep(5)
except KeyboardInterrupt:
    print("Simulation stopped.")
    client.loop_stop()
    client.disconnect()