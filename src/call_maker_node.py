import nexmo


class CallMaker:

    def __init__(self):
        self.client = nexmo.Client(key='151e8f8a', secret='OZjDCvN2Nk6TDFcD')
        
    def makingAPhoneCall(self):
        print("ooh")
        response = self.client.create_call({
            'to': [{'type': 'phone', 'number': '37255570211'}],
            'from': {'type': 'phone', 'number': 'NEXMO'},
            'answer_url': ['https://nexmo-community.github.io/ncco-examples/first_call_talk.json']})         