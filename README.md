# home-automation

Upload the mqtt_esp8266.ino file into your NodeMCU.
Enter your wifi name and password in their respective places and assign your raspberry pi's ip address to the mqtt_server variable.

Next, install mosquitto server and client on your pi, and install paho mqtt library for python.

Run the mqtt_publish code to turn on or off the inbuilt LED on your NodeMCU, or edit the code to control any pin you want.

Run the mqtt_subscribe code to print the messages coming from the NodeMCU, or edit the code to write to a text file or whatever.
