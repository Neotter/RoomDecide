#!/usr/bin/env python
# coding:utf-8
from app import app
import json
import paho.mqtt.client as mqtt
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#连接成功后的回调函数
#client这个回调的client实例
#userdata设置在Client()或者userdata_set()的私人的用户数据
#flags表示broker返回的flags
#rc表示连接结果
def on_connect(client, userdata, flags, rc):
    print ("roker Connect with result code " + str(rc))
    client.subscribe("beacon")

#消息推送回调函数
def on_message(client, userdata, msg):
    print ("run.app " + msg.topic + " " + str(msg.payload))
    beacon = json.loads(str(msg.payload))
    f = open('./app/static/beaconData.txt','w')
    f.write(beacon['id'])
    f.write('\n')
    f.write(beacon['raw_beacon_data'])
    f.close()

#初始化mqttclient
def init_mqtt_client():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    return client


client = init_mqtt_client()
client.connect("172.31.73.142", 1883, 65535)
client.loop_start()

app.run(debug=True)
