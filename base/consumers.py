import json
import time
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .serializers import ChatSerializer, OnlineSerializer
from . models import Chat, Online


class chatConsumer(WebsocketConsumer):

    def get_messages(self, dataa):
        user = dataa['building_id']
        my_model = Chat.objects.filter(building_id=user)
        serializer = ChatSerializer(my_model, many=True)
        for message in serializer.data:
            message["profile_id"] = {"id": Chat.objects.get(id=message["id"]).profile_id.id,
                                     "building_id": Chat.objects.get(id=message["id"]).profile_id.building_id.id,
                                     "user": Chat.objects.get(id=message["id"]).profile_id.user.id,
                                     "full_name": Chat.objects.get(id=message["id"]).profile_id.full_name,
                                     "bio": Chat.objects.get(id=message["id"]).profile_id.bio,
                                     "apartment": Chat.objects.get(id=message["id"]).profile_id.apartment,
                                     "phone_number": Chat.objects.get(id=message["id"]).profile_id.phone_number,
                                     "profile_pic": Chat.objects.get(id=message["id"]).profile_id.profile_pic.name, }

        try:
            return ({"type": "chat", "Type": "get", "info": serializer.data})
        except:
            return self.send(text_data=json.dumps({"kk": "error"}))

    def new_message(self, data):
        data = {'message': data['message'], 'profile_id': data['profile_id'],
                'building_id': data['building_id']}

        serializer = ChatSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        user = data['building_id']
        return self.get_messages({"building_id": user})

    def user(self, data):
        data_on = data['new_user']
        serializer = OnlineSerializer(data=data_on)
        if serializer.is_valid():
            serializer.save()
        Updated = self.all_online(data)
        return ({"type": "new", "data": Updated})

    def all_online(self, data):
        data = data
        my_model = Online.objects.filter(
            building_id=data["new_user"]["building_id"])
        serializer = OnlineSerializer(my_model, many=True)
        return (serializer.data)

    commands = {
        'get_messages': get_messages,
        'new_message': new_message,
        'new_user': user,
    }

    def save_message(self, event):
        serializer = ChatSerializer(data=event["data"])
        if serializer.is_valid():
            serializer.save()

    def chat_message(self, event):
        message = event["message"]
        self.send(text_data=json.dumps({
            "type": "chat",
            "message": message
        }))

    def user_connect(self, event):
        message = event["message"]
        self.send(text_data=json.dumps({
            "type": "user_connect",
            "message": message
        }))

    def user_disconnect(self, event):
        self.send(text_data=json.dumps({
            "type": "user",
            "message": "ll"
        }))
   ##################################################################################################

    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name
        self.user_id = self.scope["url_route"]["kwargs"]["id"]
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()
        time.sleep(4)
        self.send(text_data=json.dumps({"type": "user", "message": "ll"}))

    def send_message(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message
            }
        )

    def send_online(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "user_connect",
                "message": message
            }
        )

    def send_offline(self):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "user_disconnect",
                "message": "lllll"
            }
        )

    def receive(self, text_data):
        print("////////////////////////////////////////////////////////////////////////////////////")
        data = json.loads(text_data)
        message = self.commands[data["command"]](self, data)
        if message["type"] == "new":
            self.send_online(message["data"])
        else:
            print("ooops!")
            self.send_message(message)

    def disconnect(self, close_code):

        my_model = Online.objects.get(profile_id=self.user_id)
        my_model.delete()
        self.send_offline()
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )
