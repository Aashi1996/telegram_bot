import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Connect code here

    async def disconnect(self, close_code):
        # Disconnect code here

    async def receive(self, text_data):
        # Receive and process messages here
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        if message == '/start':
            keyboard = {
                'keyboard': [
                    ['stupid'],
                    ['fat'],
                    ['dumb'],
                ],
                'one_time_keyboard': True,
                'resize_keyboard': True
            }
            await self.send_response('Select a button:', keyboard)
        elif message in ['stupid', 'fat', 'dumb']:
            # Call a function to retrieve and send the appropriate joke
            joke = get_joke(message)
            await self.send_response(joke)

    async def send_response(self, message, reply_markup=None):
        response = {
            'message': message,
            'reply_markup': reply_markup,
        }
        await self.send(json.dumps(response))
