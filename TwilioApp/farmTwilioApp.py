import requests
import json
from flask import Flask, request, redirect
import twilio.twiml

r = requests.get('https://farmsd.firebaseio.com/modules.json')

data = r.json()

parsedDataA = 'Module A: \n' + data['A']['one']['name'] + " : " + data['A']['one']['value'] + '\n' + data['A']['two']['name'] + " : " + data['A']['two']['value'] + '\n' + data['A']['three']['name'] + " : " + data['A']['three']['value'] + '\n' + data['A']['four']['name'] + " : " + data['A']['four']['value'] + '\n' + data['A']['five']['name'] + " : " + data['A']['five']['value'] + '\n' + data['A']['six']['name'] + " : " + data['A']['six']['value'] + '\n' + data['A']['seven']['name'] + " : " + data['A']['seven']['value'] + '\n'
parsedDataB = 'Module B: \n' + data['B']['one']['name'] + " : " + data['B']['one']['value'] + '\n' + data['B']['two']['name'] + " : " + data['B']['two']['value'] + '\n' + data['B']['three']['name'] + " : " + data['B']['three']['value'] + '\n' + data['B']['four']['name'] + " : " + data['B']['four']['value'] + '\n' + data['B']['five']['name'] + " : " + data['B']['five']['value'] + '\n' + data['B']['six']['name'] + " : " + data['B']['six']['value'] + '\n' + data['B']['seven']['name'] + " : " + data['B']['seven']['value'] + '\n'
parsedDataC = 'Module C: \n' + data['C']['one']['name'] + " : " + data['C']['one']['value'] + '\n' + data['C']['two']['name'] + " : " + data['C']['two']['value'] + '\n' + data['C']['three']['name'] + " : " + data['C']['three']['value'] + '\n' + data['C']['four']['name'] + " : " + data['C']['four']['value'] + '\n' + data['C']['five']['name'] + " : " + data['C']['five']['value'] + '\n' + data['C']['six']['name'] + " : " + data['C']['six']['value'] + '\n' + data['C']['seven']['name'] + " : " + data['C']['seven']['value'] + '\n'
parsedDataD = 'Module D: \n' + data['D']['one']['name'] + " : " + data['D']['one']['value'] + '\n' + data['D']['two']['name'] + " : " + data['D']['two']['value'] + '\n' + data['D']['three']['name'] + " : " + data['D']['three']['value'] + '\n' + data['D']['four']['name'] + " : " + data['D']['four']['value'] + '\n' + data['D']['five']['name'] + " : " + data['D']['five']['value'] + '\n' + data['D']['six']['name'] + " : " + data['D']['six']['value'] + '\n' + data['D']['seven']['name'] + " : " + data['D']['seven']['value'] + '\n'
parsedDataE = 'Module E: \n' + data['E']['one']['name'] + " : " + data['E']['one']['value'] + '\n' + data['E']['two']['name'] + " : " + data['E']['two']['value'] + '\n' + data['E']['three']['name'] + " : " + data['E']['three']['value'] + '\n' + data['E']['four']['name'] + " : " + data['E']['four']['value'] + '\n' + data['E']['five']['name'] + " : " + data['E']['five']['value'] + '\n' + data['E']['six']['name'] + " : " + data['E']['six']['value'] + '\n' + data['E']['seven']['name'] + " : " + data['E']['seven']['value'] + '\n'

print parsedDataA
print parsedDataB
print parsedDataC
print parsedDataD
print parsedDataE

app = Flask(__name__)


callers = {
    "+19543974214": "Demian",
    "+18632557155": "Hunter",
    "+17577496498": "Chris",
}

modules = {
    "A": parsedDataA,
    "B": parsedDataB,
    "C": parsedDataC,
    "D": parsedDataD,
    "E": parsedDataE,
}
 
@app.route("/", methods=['GET', 'POST'])
def farmText():
    module_request = request.values.get('Body', None)
    from_number = request.values.get('From', None)

    if from_number in callers:
    	if module_request in modules:
    		message = modules[module_request]
    	else:
    		message = "Good try " + callers[from_number] + ', that module is offline'
    else:
    	if module_request in modules:
    		message = modules[module_request]
    	else:
    		message = "The module you requested is offline"
 
    resp = twilio.twiml.Response()
    resp.message(message)
 
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)