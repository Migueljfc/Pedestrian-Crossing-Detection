import paho.mqtt.client as mqtt
import json
import time
import socket

import os

import sys



def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))


def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid) )
    pass


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)


rsu = mqtt.Client("Rsu")

rsu.on_connect = on_connect
rsu.on_message=on_message
rsu.on_publish = on_publish
rsu.on_subscribe = on_subscribe
rsu.connect("192.168.0.10")
rsu.loop_start()

car1 = mqtt.Client("Car1")

car1.on_connect = on_connect
car1.on_message=on_message
car1.on_publish = on_publish
car1.on_subscribe = on_subscribe
car1.connect("192.168.0.20")
car1.loop_start()

car2 = mqtt.Client("Car2")

car2.on_connect = on_connect
car2.on_message=on_message
car2.on_publish = on_publish
car2.on_subscribe = on_subscribe
car2.connect("192.168.0.30")
car2.loop_start()

car3 = mqtt.Client("Car3")

car3.on_connect = on_connect
car3.on_message=on_message
car3.on_publish = on_publish
car3.on_subscribe = on_subscribe
car3.connect("192.168.0.40")
car3.loop_start()

s=socket.socket()
host='10.0.0.1'
port=7000 
s.bind((host,port))


f = open('/home/miguel/Documents/Pedestrian-Crossing-Detection/simulador/cam1.json')
cam1 = json.load(f)
f = open('/home/miguel/Documents/Pedestrian-Crossing-Detection/simulador/cam2.json')
cam2 = json.load(f)
f = open('/home/miguel/Documents/Pedestrian-Crossing-Detection/simulador/cam3.json')
cam3 = json.load(f)

f = open('/home/miguel/Documents/Pedestrian-Crossing-Detection/simulador/cpm.json')
cpm = json.load(f)

f = open('/home/miguel/Documents/Pedestrian-Crossing-Detection/simulador/denm.json')
denm = json.load(f)

#rsu.subscribe("vanetza/out/cpm")
rsu.publish("vanetza/in/cpm",json.dumps(cpm))

car1.subscribe("vanetza/out/cam")
car2.subscribe("vanetza/out/cam")
car3.subscribe("vanetza/out/cam")

car1.subscribe("vanetza/out/cpm")
car2.subscribe("vanetza/out/cpm")
car3.subscribe("vanetza/out/cpm")

car1.publish("vanetza/in/cam",json.dumps(cam1)) 
car2.publish("vanetza/in/cam",json.dumps(cam2)) 
car3.publish("vanetza/in/cam",json.dumps(cam3)) 

car1.subscribe("vanetza/out/denm")
car2.subscribe("vanetza/out/denm")
car3.subscribe("vanetza/out/denm")

car1Lat = 0.0
car2Lat = 0.0
car3Lat = 0.0
car1Long = 0.0
car2Long = 0.0
car3Long = 0.0
#Server is ready to accept client connection requests
platooning = False

s.listen(1)
s.setblocking(0)
try:
    while(1):
        while True:
            try:
                c,addr=s.accept()

                print ('Client connected' + str(addr))
            
                content=c.recv(100).decode()
            
                i = (int)(content)
                print("Received" + str(i))
                if  content != "":         
                    cpm['generationDeltaTime'] = time.time()
                    cpm['numberOfPerceivedObjects'] = i
                    rsu.publish("vanetza/in/cpm",json.dumps(cpm))
                    if(i>0):
                        platooning = True
                    break
            except:
                break
        
        if(platooning):
            print("Platooning...")
            if(car1Lat>car2Lat and car1Lat>car3Lat):   
                denm['originatingStationID'] = 1
                denm["longitude"] = car1Long
                denm["latitude"] = car1Lat
                car1.publish("vanetza/in/denm",json.dumps(denm)) 
            elif(car2Lat>car1Lat and car2Lat>car3Lat):
                denm['originatingStationID'] = 2
                denm["longitude"] = car2Long
                denm["latitude"] = car2Lat
                car2.publish("vanetza/in/denm",json.dumps(denm)) 
            else:         
                denm['originatingStationID'] = 3
                denm["longitude"] = car3Long
                denm["latitude"] = car3Lat
                car3.publish("vanetza/in/denm",json.dumps(denm)) 

        long = cam1["longitude"] 
        lat = cam1["latitude"] 
        long = long + 0.000030000
        lat = lat + 0.000050000
        car1Lat = lat
        car1Long = long
        
        if(lat > 40.63051088085012 ):
            print("Car1 Restart Position")
            long = -8.65215131308967
            lat = 40.62686180093694
            car1Lat = lat
            car1Long = long
        cam1["longitude"] = long
        cam1["latitude"] = lat
        car1.publish("vanetza/in/cam",json.dumps(cam1)) 
        #time.sleep(4) 

        long = cam2["longitude"] 
        lat = cam2["latitude"] 
        long = long + 0.000030000
        lat = lat + 0.000050000
        car2Lat = lat
        car2Long = long
        if(lat > 40.63051088085012 ):
            print("Car2 Restart Position")
            long = -8.65215131308967
            lat = 40.62686180093694
            car2Lat = lat
            car2Long = long
        cam2["longitude"] = long
        cam2["latitude"] = lat
        car2.publish("vanetza/in/cam",json.dumps(cam2)) 
        #time.sleep(4) 

        long = cam3["longitude"] 
        lat = cam3["latitude"] 
        long = long + 0.000030000
        lat = lat + 0.000050000
        car3Lat = lat
        car3Long = long
        if(lat > 40.63051088085012 ):
            print("Car3 Restart Position")
            long = -8.65215131308967
            lat = 40.62686180093694
            car1Lat = lat
            car1Long = long
        cam3["longitude"] = long
        cam3["latitude"] = lat
        
        car3.publish("vanetza/in/cam",json.dumps(cam3)) 
        #time.sleep(4) 

        #pedestrian crossing 
        if(platooning):
            if(car1Lat > 40.63032290439873 or car2Lat > 40.63032290439873 or car3Lat > 40.63032290439873): 
                time.sleep(10)
            platooning = False
        time.sleep(1)
except KeyboardInterrupt:  
    car1.loop_stop()
    car2.loop_stop()
    car3.loop_stop()
    rsu.loop_stop()
    car1.disconnect()
    car2.disconnect()
    car3.disconnect()
    rsu.disconnect()


