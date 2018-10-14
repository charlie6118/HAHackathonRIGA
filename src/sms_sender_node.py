import RPi.GPIO as GPIO
import time
import nexmo
import requests

#url = 'https://XXX/XX/XXX'

#button_state = {'GREEN_BUTTON': value1 = 0, 'YELLOW_BUTTON': value1 = 0, 'RED_BUTTON': value1 = 0}

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Yellow Button
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Red Button
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Green Button

IMOKAY = False


class SMSsender:
    def __init__(self):
        self.client = nexmo.Client(key='151e8f8a', secret='OZjDCvN2Nk6TDFcD')

    def sendingSMSMessage(self, msg):
        print('send')

        #if msg = '':
        #    response = self.client.send_message({'from': 'NEXMO', 'to': '37255570211', 'text': 'Grandparents need you'})
        #else:
        #    response = self.client.send_message({'from': 'NEXMO', 'to': '37255570211', 'text': msg})
            
        #response = response['messages'][0]
        
        #if response['status'] == '0':
        #    print 'Sent message', response['message-id']
        #    print 'Remaining balance is', response['remaining-balance']
        #else:
        #    print 'Error:', response['error-text']

    def makePhoneCall(self):
        print('calling')
        #response = self.client.create_call('to':[{'type': 'phone', 'number': '148433123'}],
        #                              'from': {'type': 'phone', 'number': '37255570211'})

def main():
    
    s = SMSsender()
    
    while True:
        
        localTime = time.gmtime()

        YELLOW_BUTTON_STATE = GPIO.input(18)
        RED_BUTTON_STATE = GPIO.input(17)
        GREEN_BUTTON_STATE = GPIO.input(4)

        # send the SMS
        if YELLOW_BUTTON_STATE == False:
            print('YELLOW Buttoms pressed')
        #    s.sendingSMSMessage()
            time.sleep(1)

        # IMOKAY, ALL GOOD
        elif RED_BUTTON_STATE == False:
            print('RED Buttoms pressed')
            time.sleep(1)

        # if grandparents not press the button after XXX time range
        #elif GREEN_BUTTON_STATE == True and (localTime.tm_hour > 8 or localTime.tm_hour < 20): 
        #    print('RED Buttoms pressed')
        #    s.sendingSMSMessage('IM NOT OKAY')
        #    time.sleep(1)
            

        # Make an emergency call
        elif GREEN_BUTTON_STATE == False:
            print('GREEN Buttoms pressed')
        #    s.makePhoneCall('sdfsdfa')
        #    s.sendingSMSMessage('IM NOT OKAY')
            time.sleep(1)

        # check per second 
        else:
            print('Buttoms not pressed')
            time.sleep(1)
            

if __name__ == '__main__':
    main()
