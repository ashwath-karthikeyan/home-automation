import paho.mqtt.client as mqtt
from time import sleep

broker = "192.168.1.3"  
port = 1883

def on_connect(client, userdata, flags, errors):
    if errors == 0:
        global connected
        connected = True

def on_message(client, userdata, message):
    message.payload = message.payload.decode("utf-8")
    print (str(message.payload))

connected = False

client = mqtt.Client("subscribing")
client.on_connect= on_connect
client.on_message= on_message

client.connect(broker, port)

client.loop_start()

client.subscribe("outTopic")

while True:
    client.on_message
    sleep(0.1)