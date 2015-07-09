import json
import requests
import threading
import datetime
import logging

import config
import mac_notifier

def visa_request():
	url = "http://idata.com.tr/track" 
	url += "/" + config.country_code
	url += "/" + config.application_id
	url += "/" + config.passport_id

	response = requests.post(url)
	json_text = response.text[23:-2]
	json_data = json.loads(json_text)
	return json_data["state"]

def check_visa():
	visa_response = visa_request().encode('utf-8')
	logging.info(visa_response)
	title = "VISA " + config.application_id
	mac_notifier.notify(title, visa_response)
	threading.Timer(300, check_visa).start()


logging.basicConfig(filename='visa_application.log',format='%(levelname)s:%(asctime)s %(message)s',level=logging.INFO)
check_visa()
