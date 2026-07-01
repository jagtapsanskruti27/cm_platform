import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User

from .models import Message


# ==================================================
# GENERAL CHAT
# ==================================================

class GeneralChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):

        self.group_name = "general_chat"

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):

        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):

        data = json.loads(text_data)

        # typing
        if data.get("type") == "typing":

            await self.channel_layer.group_send(
                self.group_name,
                {
                    "type": "typing_message",
                    "user": self.scope["user"].username
                }
            )
            return

        # message
        if data.get("type") == "message":

            text = data.get("message")

            if not text:
                return

            await self.save_general_message(text)

            await self.channel_layer.group_send(
                self.group_name,
                {
                    "type": "chat_message",
                    "message": text,
                    "sender": self.scope["user"].username
                }
            )

    async def chat_message(self, event):

        await self.send(
            text_data=json.dumps({
                "message": event["message"],
                "sender": event["sender"]
            })
        )

    async def typing_message(self, event):

        await self.send(
            text_data=json.dumps({
                "typing": event["user"]
            })
        )

    @database_sync_to_async
    def save_general_message(self, text):

        Message.objects.create(
            sender=self.scope["user"],
            text=text,
            group_name="general"
        )


# ==================================================
# PRIVATE CHAT
# ==================================================

class PrivateChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):

        self.room = self.scope["url_route"]["kwargs"]["room"]

        await self.channel_layer.group_add(
            self.room,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):

        await self.channel_layer.group_discard(
            self.room,
            self.channel_name
        )

    async def receive(self, text_data):

        data = json.loads(text_data)

        # typing
        if data.get("type") == "typing":

            await self.channel_layer.group_send(
                self.room,
                {
                    "type": "typing_private",
                    "user": self.scope["user"].username
                }
            )
            return

        # message
        if data.get("type") == "message":

            text = data.get("message")

            receiver = data.get("receiver")

            if not text:
                return

            await self.save_private_message(
                text,
                receiver
            )

            await self.channel_layer.group_send(
                self.room,
                {
                    "type": "private_message",
                    "message": text,
                    "sender": self.scope["user"].username
                }
            )

    async def private_message(self, event):

        await self.send(
            text_data=json.dumps({
                "message": event["message"],
                "sender": event["sender"]
            })
        )

    async def typing_private(self, event):

        await self.send(
            text_data=json.dumps({
                "typing": event["user"]
            })
        )

    @database_sync_to_async
    def save_private_message(self, text, receiver_id):

        receiver = User.objects.get(id=receiver_id)

        Message.objects.create(
            sender=self.scope["user"],
            receiver=receiver,
            text=text,
            group_name=self.room
        )