import random
from paho.mqtt import client as mqtt_client
import time 

while (True):
    def on_connect(client, userdata, flag, rc):
        if rc==0:
            print ("Client is connected")
            global connected 
            connected=True
        else:
            print("connection failed")

    connected=False
    broker_address="192.168.229.212"
    port=1883
    client_id = f'python-mqtt-{random.randint(0, 100)}'

    client=mqttclient.Client(client_id)
    client.on_connect=on_connect
    client.connect(broker_address, port=port)
    client.loop_start

    while connected!=True:
        time.sleep(0.2)

    client.publish("mqtt/topic", "hello mqtt")
    client.loop_stop()
