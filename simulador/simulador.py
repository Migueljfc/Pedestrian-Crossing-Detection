#from ntpath import join
import paho.mqtt.client as mqtt
#from denm import denm
import cam
import json

mqttc = mqtt.Client()
mqttc.connect("192.168.98.10")
cam1 = cam
cam1 = {"accEngaged": True,
    "acceleration": 0,
    "altitude": 800001,
    "altitudeConf": 15,
    "brakePedal": True,
    "collisionWarning": True,
    "cruiseControl": True,
    "curvature": 1023,
    "driveDirection": "FORWARD",
    "emergencyBrake": True,
    "gasPedal": False,
    "heading": 3601,
    "headingConf": 127,
    "latitude": 400000000,
    "length": 100,
    "longitude": -80000000,
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
    "stationID": 1,
    "stationType": 15,
    "width": 30,
    "yawRate": 0}


ret= mqttc.publish("vanetza/in/cam",json.dumps(cam1))

cam1["longitude"] = 2

ret= mqttc.publish("vanetza/in/cam",json.dumps(cam1))
