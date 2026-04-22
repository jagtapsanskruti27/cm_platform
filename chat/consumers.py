import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        room_info = self.scope['url_route']['kwargs']
        print(f"WebSocket connect attempt for room: {room_info}")
        self.room = self.scope['url_route']['kwargs']['room']
        self.room_group = "chat_" + self.room

        # Check authentication
        user = self.scope.get('user')
        print(f"User: {user}, Is authenticated: {user.is_authenticated if user else False}")

        await self.channel_layer.group_add(
            self.room_group,
            self.channel_name
        )

        await self.accept()
        print("WebSocket connection accepted")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)

        message_type = data.get('type', 'message')

        if message_type == 'message':
            await self.channel_layer.group_send(
                self.room_group,
                {
                    'type': 'chat_message',
                    'message': data['message'],
                    'sender': self.scope['user'].username if self.scope['user'].is_authenticated else 'Anonymous'
                }
            )
        elif message_type == 'typing':
            await self.channel_layer.group_send(
                self.room_group,
                {
                    'type': 'user_typing',
                    'user': data['user']
                }
            )
        elif message_type == 'image':
            await self.channel_layer.group_send(
                self.room_group,
                {
                    'type': 'chat_image',
                    'image': data['image'],
                    'sender': self.scope['user'].username if self.scope['user'].is_authenticated else 'Anonymous'
                }
            )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender': event['sender']
        }))

    async def user_typing(self, event):
        await self.send(text_data=json.dumps({
            'typing': event['user'] + ' is typing...'
        }))

    async def chat_image(self, event):
        await self.send(text_data=json.dumps({
            'image': event['image'],
            'sender': event['sender']
        }))
