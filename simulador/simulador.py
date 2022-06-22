#from ntpath import join
from pickletools import long1
import paho.mqtt.client as mqtt
#from denm import denm
import cam
import json
import time

""" def connect_mqtt(broker):
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(broker)
    return client """


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



    
""" mqttc = mqtt.Client()
mqttc.connect("192.168.98.10") """
#mqttc = connect_mqtt("192.168.98.10")

car1 = mqtt.Client("Car1")

car1.on_connect = on_connect
car1.on_message=on_message
car1.on_publish = on_publish
car1.on_subscribe = on_subscribe
car1.connect("192.168.98.20")
car1.loop_start()

car2 = mqtt.Client("Car2")

car2.on_connect = on_connect
car2.on_message=on_message
car2.on_publish = on_publish
car2.on_subscribe = on_subscribe
car2.connect("192.168.98.30")
car2.loop_start()

car3 = mqtt.Client("Car3")

car3.on_connect = on_connect
car3.on_message=on_message
car3.on_publish = on_publish
car3.on_subscribe = on_subscribe
car3.connect("192.168.98.40")
car3.loop_start()

cam1 = cam
cam1 = {"accEngaged": True,
    "acceleration": 5,
    "altitude": 0,
    "altitudeConf": 15,
    "brakePedal": False,
    "collisionWarning": False,
    "cruiseControl": False,
    "curvature": 1023,
    "driveDirection": "FORWARD",
    "emergencyBrake": False,
    "gasPedal": True,
    "heading": 3601,
    "headingConf": 127,
    "latitude": 40.62971, 
    "length": 100,
    "longitude": -8.65351,
    "semiMajorConf": 4095,
    "semiMajorOrient": 3601,
    "semiMinorConf": 4095,
    "specialVehicle": {
        "publicTransportContainer": {
            "embarkationStatus": False
        }
    },
    "speed": 16383,
    "speedConf": 127,
    "speedLimiter": True,
    "stationID": 2,
    "stationType": 5,
    "width": 30,
    "yawRate": 0}

cam2 = cam
cam2 = {"accEngaged": True,
    "acceleration": 5,
    "altitude": 0,
    "altitudeConf": 15,
    "brakePedal": False,
    "collisionWarning": False,
    "cruiseControl": False,
    "curvature": 1023,
    "driveDirection": "FORWARD",
    "emergencyBrake": False,
    "gasPedal": True,
    "heading": 3601,
    "headingConf": 127,
    "latitude": 40.62991, 
    "length": 100,
    "longitude": -8.65371,
    "semiMajorConf": 4095,
    "semiMajorOrient": 3601,
    "semiMinorConf": 4095,
    "specialVehicle": {
        "publicTransportContainer": {
            "embarkationStatus": False
        }
    },
    "speed": 16383,
    "speedConf": 127,
    "speedLimiter": True,
    "stationID": 2,
    "stationType": 5,
    "width": 30,
    "yawRate": 0}

cam3 = cam
cam3 = {"accEngaged": True,
    "acceleration": 5,
    "altitude": 0,
    "altitudeConf": 15,
    "brakePedal": False,
    "collisionWarning": False,
    "cruiseControl": False,
    "curvature": 1023,
    "driveDirection": "FORWARD",
    "emergencyBrake": False,
    "gasPedal": True,
    "heading": 3601,
    "headingConf": 127,
    "latitude": 40.63001, 
    "length": 100,
    "longitude": -8.65391,
    "semiMajorConf": 4095,
    "semiMajorOrient": 3601,
    "semiMinorConf": 4095,
    "specialVehicle": {
        "publicTransportContainer": {
            "embarkationStatus": False
        }
    },
    "speed": 16383,
    "speedConf": 127,
    "speedLimiter": True,
    "stationID": 2,
    "stationType": 5,
    "width": 30,
    "yawRate": 0}

car1.subscribe("vanetza/out/cam")
car2.subscribe("vanetza/out/cam")
car3.subscribe("vanetza/out/cam")

car1.publish("vanetza/in/cam",json.dumps(cam1)) 
car2.publish("vanetza/in/cam",json.dumps(cam2)) 
car3.publish("vanetza/in/cam",json.dumps(cam3)) 

while(1):
    long = cam1["longitude"] 
    lat = cam1["latitude"] 
    long = long + 0.00010
    lat = lat + 0.00008
    cam1["longitude"] = long
    cam1["latitude"] = lat
    if(lat > 40.63040 and long > -8.65399):
        print("restart")
    car1.publish("vanetza/in/cam",json.dumps(cam1)) 
    time.sleep(4) 

    long = cam2["longitude"] 
    lat = cam2["latitude"] 
    long = long + 0.00010
    lat = lat + 0.00008
    cam2["longitude"] = long
    cam2["latitude"] = lat
    if(lat > 40.63040 and long > -8.65399):
        print("restart")
    car2.publish("vanetza/in/cam",json.dumps(cam2)) 
    time.sleep(4) 

    long = cam3["longitude"] 
    lat = cam3["latitude"] 
    long = long + 0.00010
    lat = lat + 0.00008
    cam3["longitude"] = long
    cam3["latitude"] = lat
    if(lat > 40.63040 and long > -8.65399):
        print("restart")
    car3.publish("vanetza/in/cam",json.dumps(cam3)) 
    time.sleep(4) 


car1.loop_stop()
car2.loop_stop()
car3.loop_stop()


#ret= mqttc.publish("vanetza/in/cam",json.dumps(cam1))
