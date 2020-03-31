# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class GameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'gameplay'
        self.room_group_name = 'players'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        print("CHANNEL NAME", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print("DATA", text_data)
        message = text_data_json['message']

        # Send message to room group
        print("Sending MESSAGE!!!!")

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'game.message',
                'message': message
            }
        )

    # Receive message from room group
    async def game_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'type': 'message',
            'message': message
        }))