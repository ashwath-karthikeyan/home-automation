import paho.mqtt.client as mqtt
from time import sleep

broker = "192.168.1.3"
port = 1883

def on_connect(client, userdata, flags, errors):
    if errors == 0:
        global connected
        connected = True 
        
def on_publish(client,userdata,result):
    pass

def on():
    client.publish("inTopic", "1")

def off():
    client.publish("inTopic", "0")

connected = False

client= mqtt.Client("publishing")
client.on_publish = on_publish

client.connect(broker, port)

while True:
    a = int(input("Enter value:  "))

    if a == 1:
        on()
    
    else:
        off()

# client.publish("inTopic", "0")