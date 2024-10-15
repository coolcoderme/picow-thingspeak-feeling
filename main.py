import machine
import urequests 
from machine import Pin
import network, time
import picozero
from picozero import Button
 
angry = Button(19)
sad = Button (16)
happy = Button (17)
disgust = Button (18)
fear = Button (15)

thingspeakid = "" #thingspeak id
ssid = '' #ssid
password = ''#password

# Configure Pico W as Station
sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)
 
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.connect(ssid, password)
    while not sta_if.isconnected():
     pass
print('network config:', sta_if.ifconfig())

def angrysend():
    import urequests
    request = urequests.post( 'https://api.thingspeak.com/update?api_key='+ thingspeakid +'&field3=1')
    request.close()
    print ("u r angry!!")
    
def sadsend():
    import urequests
    request = urequests.post( 'https://api.thingspeak.com/update?api_key='+ thingspeakid + '&field1=1')
    request.close()
    print ("u r sad!!")

def happysend():
    import urequests
    request = urequests.post( 'https://api.thingspeak.com/update?api_key='+ thingspeakid +'&field2=1')
    request.close()
    print ("u r happy!!")

def disgustsend():
    import urequests
    request = urequests.post( 'https://api.thingspeak.com/update?api_key='+ thingspeakid +'&field5=1')
    request.close()
    print ("u r disgusted!!")

def fearsend():
    import urequests
    request = urequests.post( 'https://api.thingspeak.com/update?api_key='+ thingspeakid +'&field4=1')
    request.close()
    print ("u r scared!!")

while True:
    angry.when_pressed = angrysend
    sad.when_pressed = sadsend
    happy.when_pressed = happysend
    disgust.when_pressed = disgustsend
    fear.when_pressed = fearsend
