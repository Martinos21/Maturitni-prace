import paho.mqtt.client as mqtt

def on_connect (client, userdata, flags, rc):
    print ("Connected with code:" +str(rc))
    client.subscribe("mytopic/#")

def on_message (client, userdata, msg):
    print(str(msg.payload))


client=mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtts://IEZ000246.mqtt.ioteasyconnect.cz", 1883, 60)
client.username_pw_set("IEZ000246:901288910037540", "Encantr1892!")

client.loop_forever()