import RPi.GPIO as GPIO
import time
import nexmo
#import twilio
import requests

GPIO.setmode(GPIO.BCM)
chanA_list = [4,18,17]
client = nexmo.Client(key='151e8f8a', secret='OZjDCvN2Nk6TDFcD')
GPIO.setup(chanA_list, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(04, GPIO.IN, pull_up_down=GPIO.PUD_UP)


class SMSsender:

    def __init__(self):
        pass
    
    def sendingOutMessage(self, flag):
        if flag == "Green":
            message = 'I am good. Do not worry, be happy'
        elif flag == "Yellow":
            message = 'Please call me'
        ##response = client.send_message({'from': '3725504560', 'to': '37255570211', 'text': 'Screw You'})
        response = client.send_message({'from': 'NEXMO', 'to': '37255570211', 'text': message})
        
        response = response['messages'][0]
        
        if response['status'] == '0':
            print 'Sent message', response['message-id']
            print 'Remaining balance is', response['remaining-balance']
            ##write over here website post
        else:
            print 'Error:', response['error-text']

class CallMaker:

    def __init__(self):
        pass

    def makingAPhoneCall(self):
        print("ooh")
        response = client.create_call({
            'to': [{'type': 'phone', 'number': '37255570211'}],
            'from': {'type': 'phone', 'number': 'NEXMO'},
            'answer_url': ['https://nexmo-community.github.io/ncco-examples/first_call_talk.json']})         

s = SMSsender()

#c = CallMaker()

#create an file called button.txt
#
#
while True:
    input_state_green=GPIO.input(4) 
    input_state_yellow=GPIO.input(18) 
    input_state_red=GPIO.input(17) 
    if(input_state_green==0):        #print(input_state_green)
        #print("Green")
        #makingAPhoneCall()
        #sendingOutMessage()
        #s.sendingOutMessage("Green")
        time.sleep(0.5)
        req = requests.get('http://test.developerforwebsites.com/button.php/')
        
    elif(input_state_yellow==0):
        #print(input_state_yellow)
        #print("Yellow")
        #makingAPhoneCall()
        #s.sendingOutMessage("Yellow")
        #sendingRequestToWebsite():
        time.sleep(0.5)
        req = requests.get('http://test.developerforwebsites.com/yes.php/')
        
        
    elif(input_state_red==0):
        #print(input_state_red)
        print("Red")
        #c.makingAPhoneCall()
        time.sleep(0.5)
        #req = requests.get('')
    else:
        print("no button is pressed")
        time.sleep(0.3)
        
##Welcome@RTU
