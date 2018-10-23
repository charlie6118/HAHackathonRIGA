import RPi.GPIO as GPIO
import time
import requests
import json
from src.sms_sender_node import SMSsender
from src.call_maker_node import CallMaker

GPIO.setmode(GPIO.BCM)
chanA_list = [4,18,17]
GPIO.setup(chanA_list, GPIO.IN, pull_up_down=GPIO.PUD_UP)

IMOKAY = False


def main():

    data = {"red": False, "green": False, "yellow": False}
    url = 'https://test.developerforwebsites.com/button.php'

    s = SMSsender()
    c = CallMaker()
    
    while True:
        
        localTime = time.gmtime()

        YELLOW_BUTTON_STATE = GPIO.input(18)
        RED_BUTTON_STATE = GPIO.input(17)
        GREEN_BUTTON_STATE = GPIO.input(4)

        # send the SMS
        if YELLOW_BUTTON_STATE == False:
            print('YELLOW Buttom pressed')
            data["yellow"] = True
            requests.get(url, json.dumps(data))
            s.sendingSMSMessage("")
            time.sleep(1)

        # IMOKAY, ALL GOOD
        elif RED_BUTTON_STATE == False:
            print('RED Buttom pressed')
            data["red"] = True
            requests.get(url, json.dumps(data))
            c.makingAPhoneCall()
            time.sleep(1)

        # Make an emergency call
        elif GREEN_BUTTON_STATE == False:
            print('GREEN Buttom pressed')
            IMOKAY = True
            data["green"] = True
            requests.get(url, json.dumps(data))
            time.sleep(1)

        # user should press the button twice, first one between 7~10, second one 18~21
        # if user not press the button in time range then send notification
        elif IMOKAY == False and ((localTime.tm_hour > 10)  or localTime.tm_hour > 21): 
           print('Not press button in time range')
           s.sendingSMSMessage('Not press button in time range')
           data["yellow"] = True
           requests.get(url, json.dumps(data))
           time.sleep(1)

        # check per second 
        else:
            print('Buttoms not pressed')
            time.sleep(1)

        if localTime.tm_hour  == 11 or localTime.tm_hour == 22:
            IMOKAY == False
            
if __name__ == '__main__':
    main()

