
import paho.mqtt.client as mqttclient
import time 

def on_connect(client,userdata,rc):
    if rc==0:
        print("client is connected")
        global connected
        connected=True
    else:
        print("client is not connected")

def on_message(client,userdata,message):
    print("Message received"+ str(message.payload.decode("utf-8")))
    print("Topic"+str(message.topic))


connected=False
Messagereceived=False

broker_address="mqtts://IEZ000246.mqtt.ioteasyconnect.cz"
port=1883
user="IEZ000246:901288910037540"
password="Encantr1892!"

client= mqttclient.Client("myclient")
client.username_pw_set(user,password=password)
client.connect(broker_address,port=port)
client.loop_start()
client.subscribe("mytopic")

while connected !=True:
    time.sleep(0.2)
while Messagereceived!=True:
    time.sleep(0.2)

client.loop_stop()