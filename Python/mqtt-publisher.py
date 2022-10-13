
import paho.mqtt.client as mqttclient
import time 


def on_connect(client, userdata, flag, rc):
    if rc==0:
        print ("Client is connected")
        global connected 
        connected=True
    else:
        print("connection failed")

connected=False
broker_address="mqtts://IEZ000246.mqtt.ioteasyconnect.cz"
port=1883
user="IEZ000246:901288910037540"
password="Encantr1892"

client=mqttclient.Client("myclient")
client.username_pw_set(user, password=password)
client.on_connect=on_connect
client.connect(broker_address, port=port)
client.loop_start

while connected!=True:
    time.sleep(0.2)

client.publish("mqtt/firstcode", "hello mqtt")
client.loop_stop()
