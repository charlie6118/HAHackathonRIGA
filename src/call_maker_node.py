import nexmo

class CallMaker:

    def __init__(self):
        self.client = nexmo.Client(key='000000', secret='00000000000')
        
    def makingAPhoneCall(self):
        print("make a phone call")
        response = self.client.create_call({
            'to': [{'type': 'phone', 'number': '37255555555'}],
            'from': {'type': 'phone', 'number': 'NEXMO'},
            'answer_url': ['https://nexmo-community.github.io/ncco-examples/first_call_talk.json']})         