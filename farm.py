from nrf24 import NRF24
import time
from time import gmtime, strftime

pipes = [[0xf0, 0xf0, 0xf0, 0xf0, 0xe1], [0xf0, 0xf0, 0xf0, 0xf0, 0xd2], [0xf0, 0xf0, 0xf0, 0xf0, ], [0xf0], [0xf0], [0xf0]]

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


def parseData (out):
	dataFromBoard = out
	value = dataFromBoard.split("_")
	return value

def toDatabase(parsedString):
	if parsedString[2] == 'one':
	   payload={'Ground Moisture 1': parsedString[0]}
	   r = requests.put(url, data=json.dumps(payload))
	   print r.text
	elif parsedString[2] == 'two':
		payload={'Ground Moisture 2': parsedString[0]}
		r = requests.put(url, data=json.dumps(payload))
		print r.text
	elif parsedString[2] == 'three':
		payload={'Ground Moisture 3': parsedString[0]}
		r = requests.put(url, data=json.dumps(payload))
		print r.text
	elif parsedString[2] == 'four':
		payload={'Temperature': parsedString[0]}
		r = requests.put(url, data=json.dumps(payload))
		print r.text
	elif parsedString[2] == 'five':
		payload={'Ground Temperature': parsedString[0]}
		r = requests.put(url, data=json.dumps(payload))
		print r.text
	elif parsedString[2] == 'six':
		payload={'Humidity': parsedString[0]}
		r = requests.put(url, data=json.dumps(payload))
		print r.text
	elif parsedString[2] == 'seven':
		payload={'Light': parsedString[0]}
		r = requests.put(url, data=json.dumps(payload))
		print r.text
	else:
	   print 'Cant Recognize Sensor'



radio.startListening()
radio.stopListening()

radio.printDetails()
radio.startListening()

while True:
    pipe = [0]
    while not radio.available(pipe, True):
        time.sleep(1000/1000000.0)
    recv_buffer = []
    radio.read(recv_buffer)
    out = ''.join(chr(i) for i in recv_buffer)
    # insert function here
    parsedData = parseData(out)
    toDatabase(parsedData)
    print out

