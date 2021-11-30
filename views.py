from django.shortcuts import render
from django.http import HttpResponse
from time import sleep

def landing(request):
    return render(request, 'homeauto.html')

def mqtt(request, status):
    import paho.mqtt.client as mqtt
    
    broker = "localhost"
    port = 1883
    client = mqtt.Client("publishing")

    def on():
        client.publish("inTopic", "1")

    def off():
        client.publish("inTopic", "0")

    connected = False

    client.connect(broker, port)

    if str(status) == "on":
        on()
    elif str(status) == "off":
        off()
    return render(request, 'homeauto.html')