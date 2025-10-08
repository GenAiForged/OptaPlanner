import paho.mqtt.client as mqtt
import requests
import json

# MQTT Broker settings
BROKER_ADDRESS = "mqtt_broker"
BROKER_PORT = 1883
TOPIC = "telemetry"

# Backend API settings
BACKEND_URL = "http://backend:8000/telemetry"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(TOPIC)
    else:
        print(f"Failed to connect, return code {rc}\n")

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload)
        print(f"Received message: {payload}")
        response = requests.post(BACKEND_URL, json=payload)
        response.raise_for_status()
        print(f"Data forwarded to backend: {response.status_code}")
    except json.JSONDecodeError:
        print("Error decoding JSON from MQTT message")
    except requests.exceptions.RequestException as e:
        print(f"Error forwarding data to backend: {e}")

client = mqtt.Client(client_id="mqtt_bridge")
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER_ADDRESS, BROKER_PORT)

client.loop_forever()