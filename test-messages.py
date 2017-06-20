#!/usr/bin/python3
# 
# test-messages.py - This script publish a random MQTT messages every 2 s.
#
# Copyright (c) 2013-2017, Fabian Affolter <fabian@affolter-engineering.ch>
# Released under the MIT license. See LICENSE file for details.
#
import random
import time
import paho.mqtt.client as mqtt

timestamp = int(time.time())

broker = '127.0.0.1'
port = 1883
element = 'home'
#areas = ['front', 'back', 'basement', 'living']
areas = ['living']
entrances = ['door', 'window']
states = ['true', 'false']

print('Messages are published on topic %s/#... -> CTRL + C to shutdown' \
    % element)

while True:
    area = random.choice(areas)
    if (area in ['basement', 'living']):
        topic = element + '/' + area + '/temp'
        message = random.randrange(0, 30, 1)
    else:
        topic = element + '/' + area + '/' + random.choice(entrances)
        message = random.choice(states)

    mqttclient = mqtt.Client("mqtt-panel-test", protocol=mqtt.MQTTv311)
    mqttclient.connect(broker, port=int(port))
    mqttclient.publish(topic, message)
    time.sleep(2)

