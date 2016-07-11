# coding:utf-8
from app import app
from flask import render_template
import json


@app.route('/')
def index():
    BeaconData = {}
    beaconDatafile = open('./app/static/beaconData.txt')
    BeaconData['id'] = beaconDatafile.readline()
    BeaconData['raw_data'] = beaconDatafile.readline()
    beaconDatafile.close()
    return render_template("index.html", title = 'RoomDecide',data = BeaconData)

@app.route('/refresh')
def refresh():
    BeaconData = {}
    beaconDatafile = open('./app/static/beaconData.txt')
    BeaconData['id'] = beaconDatafile.readline().strip('\n')
    BeaconData['raw_beacon_data'] = beaconDatafile.readline()
    beaconDatafile.close()
    BeaconData['raw_beacon_data'] = BeaconData['raw_beacon_data'][56:58]
    BeaconData = {'id':BeaconData['id'], 'raw_data':BeaconData['raw_beacon_data']}
    data_string = json.dumps(BeaconData)
    return data_string



