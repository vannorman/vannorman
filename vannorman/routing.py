from channels.routing import ProtocolTypeRouter
from channels.generic.websocket import WebsocketConsumer
import json
from django.conf.urls import url
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        self.send(text_data=json.dumps({
            'message': message
        }))
        print("hello! a message was received.")
        print(message)

websocket_urlpatterns = [
    url(r'^ws/msg/$', ChatConsumer),
]

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})



