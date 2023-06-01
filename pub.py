import time
import random
import paho.mqtt.client as mqtt

broker_address = "localhost"  # Replace with the IP address of your MQTT broker
topic = "test/topic"  # Replace with the MQTT topic you want to publish to

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
    else:
        print("Connection failed")

def on_publish(client, userdata, mid):
    print("Message published")

client.on_connect = on_connect
client.on_publish = on_publish

client.connect(broker_address)
client.loop_start()

while True:
    temperature = random.uniform(20.0, 30.0)  # Replace with your data generation logic
    payload = "Temperature: {:.2f}".format(temperature)

    client.publish(topic, payload)
    print("Published: ", payload)

    time.sleep(2)  # Sleep for 2 seconds before publishing the next message

