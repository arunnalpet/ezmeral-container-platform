import os
import sys 
import json
import requests
from time import sleep


cli_input = json.loads(sys.argv[1])
features = [] 
features.append(cli_input['xval'])

payload = {
	"instances": [features]
}

r = requests.post('http://localhost:8051/v1/models/kerasmodel:predict', json=payload)
pred = json.loads(r.content.decode('utf-8'))['predictions'][0]

#print("Chances of having diabetes: " + str(pred) + "%")
print(str(pred))