import nexmo

class SMSsender:

    def __init__(self):
        self.client = nexmo.Client(key='000000', secret='00000000000')

    def sendingSMSMessage(self, msg):
        if msg == '':
           response = self.client.send_message({'from': 'NEXMO', 'to': '37255570211', 'text': 'I need you'})
        else:
           response = self.client.send_message({'from': 'NEXMO', 'to': '37255570211', 'text': msg})
            
        response = response['messages'][0]
        
        if response['status'] == '0':
           print('Sent message', response['message-id'])
           print('Remaining balance is', response['remaining-balance'])
        else:
           print('Error:', response['error-text'])


