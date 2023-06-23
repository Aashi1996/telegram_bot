from chat.consumers import ChatConsumer

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": URLRouter([path("ws/chat/", ChatConsumer.as_asgi())]),
    }
)
