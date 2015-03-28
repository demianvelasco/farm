from nrf24 import NRF24
import time
from time import gmtime, strftime
import requests
import json


# Communication setup
pipes = [[0xf0, 0xf0, 0xf0, 0xf0, 0xe1], [0xf0, 0xf0, 0xf0, 0xf0, 0xd1], [0xf0, 0xf0, 0xf0, 0xf0, 0xd2], [0xf0, 0xf0, 0xf0, 0xf0, 0xd3], [0xf0, 0xf0, 0xf0, 0xf0, 0xd4], [0xf0, 0xf0, 0xf0, 0xf0, 0xd5]]

radio = NRF24()
radio.begin(0, 0,25,18) #set gpio 25 as CE pin
radio.setRetries(15,15)
radio.setPayloadSize(32)
radio.setChannel(0x4c)
radio.setDataRate(NRF24.BR_250KBPS)
radio.setPALevel(NRF24.PA_MAX)
radio.setAutoAck(1)
radio.openWritingPipe(pipes[0])
radio.openReadingPipe(1, pipes[1])
radio.openReadingPipe(2, pipes[2])
radio.openReadingPipe(3, pipes[3])
radio.openReadingPipe(4, pipes[4])
radio.openReadingPipe(5, pipes[5])

radio.startListening()
radio.stopListening()

radio.printDetails()
radio.startListening()


def toDatabase(value):
	url = 'https://farmsd.firebaseio.com/modules/' + value[1] + '/' + value[2] + '/.json'
	if value[2] == 'one':
	   payload = {'name': 'Ground Moisture 1', 'value': value[0]}
	   r = requests.put(url, data=json.dumps(payload))
	   print r.text
	elif value[2] == 'two':
		payload = {'name': 'Ground Moisture 2', 'value': value[0]}
		r = requests.put(url, data=json.dumps(payload))
		print r.text
	elif value[2] == 'three':
		payload = {'name': 'Ground Moisture 3', 'value': value[0]}
		r = requests.put(url, data=json.dumps(payload))
		print r.text
	elif value[2] == 'four':
		payload = {'name': 'Temperature', 'value': value[0]}
		r = requests.put(url, data=json.dumps(payload))
		print r.text
	elif value[2] == 'five':
		payload = {'name': 'Ground Temperature', 'value': value[0]}
		r = requests.put(url, data=json.dumps(payload))
		print r.text
	elif value[2] == 'six':
		payload = {'name': 'Humidity', 'value': value[0]}
		r = requests.put(url, data=json.dumps(payload))
		print r.text
	elif value[2] == 'seven':
		payload = {'name': 'Light', 'value': value[0]}
		r = requests.put(url, data=json.dumps(payload))
		print r.text
	else:
	   print 'Cant Recognize Sensor'

def sendToDatabase(out):
    value = out.split("\\0x00")
    toDatabase(value)

while True:
    pipe = [0]
    while not radio.available(pipe, True):
        time.sleep(1000/1000000.0)
    recv_buffer = []
    radio.read(recv_buffer)
    out = ''.join(chr(i) for i in recv_buffer)
    sendToDatabase(out)
    print out
