import os
import json
import bottle
import codecs

from bottle import route, run, template, error, post, request, get, response
from ouimeaux.environment import Environment

#Wemo Setup Funcs
def on_switch(switch):
    print "switch found!", switch.name


def prepEnv():
    wEnv = Environment(on_switch)
    wEnv.start()
    wEnv.discover(seconds=3)
    return wEnv

def turnDevicesOn(items):
    wEnv = prepEnv
    for item in items:
        switch = wEnv.get_switch(item)
        switch.on()


def turnDevicesOff(items):
    wEnv = prepEnv
    for item in items:
        switch = wEnv.get_switch(item)
        switch.off()




# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))

@route('/')
def index():
    return template('index.html')


@route('/api/on/<device>')
def wemoOn(device):
    wEnv = prepEnv()
    switch = wEnv.get_switch(device)
    switch.on()
    return "Device: " + device + " has been turned on"

@route('/api/off/<device>')
def wemoOff(device):
    wEnv = prepEnv()
    switch = wEnv.get_switch(device)
    switch.off()
    return "Device: " + device + " has been turned off"


@route('/api/status/<device>')
def wemoStatus(device):
    wEnv = prepEnv()
    tmpDevice = wEnv.get_switch(device)
    tmpDeviceStatus = tmpDevice.get_state
    if tmpDeviceStatus:
        return "Device: " + device + " is on!"
    else:
        return "Device: " + device + " is off!"


@get('/api/getdevices')
def getDeviceList():
    try:
        wEnv = prepEnv()
        response.headers['Content-Type'] = 'application/json'
        response.headers['Cache-Control'] = 'no-cache'
        response.status = 200
        return json.dumps({'devices':list(wEnv.list_switches())})

    except:
        request.status = 400
        return



@post('/api/deviceactions')
def wemoActionsHandler():
    #Handles Multiple Actions at Once
    try:
        #decode json
        try:
            # data = request.json()
            # sender = request.json['sender']
            # receiver = request.json['receiver']
            data = request.json
            print data
        except:
            print "could not decode json"
            raise ValueError
        
        if data is None:
            print "data is none for device actions"
            raise ValueError
        
        turnDevicesOn(data['devicesToTurnOn'])
        turnDevicesOff(data['devicesToTurnOff'])
        response.content_type = 'application/json'
        request.status = 200
        return

    except:
        response.status = 400
        return

    









    wEnv = prepEnv()





# ... build or import your bottle application here ...
# Do NOT use bottle.run() with mod_wsgi
bottle.debug(True)
application = bottle.default_app()
