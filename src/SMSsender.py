import nexmo

class SMSsender:

    def __init__(self):
        self.client = nexmo.Client(key='151e8f8a', secret='OZjDCvN2Nk6TDFcD')
    
    def sendingOutMessage(self, flag):
        if flag == "Green":
            message = 'I am good. Do not worry, be happy'
        elif flag == "Yellow":
            message = 'Please call me'
        response = self.client.send_message({'from': 'NEXMO', 'to': '37255570211', 'text': message})
        
        response = response['messages'][0]
        
        if response['status'] == '0':
            print 'Sent message', response['message-id']
            print 'Remaining balance is', response['remaining-balance']

        else:
            print 'Error:', response['error-text']
