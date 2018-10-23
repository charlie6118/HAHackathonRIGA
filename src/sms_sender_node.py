import RPi.GPIO as GPIO
import time
import nexmo
import requests
import json

data = {"red": False, "green": False, "yellow": False}
url = 'https://test.developerforwebsites.com/button.php'

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Yellow Button
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Red Button
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Green Button

IMOKAY = False

class SMSsender:
    def __init__(self):
        self.client = nexmo.Client(key='151e8f8a', secret='OZjDCvN2Nk6TDFcD')

    def sendingSMSMessage(self, msg):

        if msg == '':
           response = self.client.send_message({'from': 'NEXMO', 'to': '37255570211', 'text': 'I need you'})
        else:
           response = self.client.send_message({'from': 'NEXMO', 'to': '37255570211', 'text': msg})
            
        response = response['messages'][0]
        
        if response['status'] == '0':
           print 'Sent message', response['message-id']
           print 'Remaining balance is', response['remaining-balance']
        else:
           print 'Error:', response['error-text']


