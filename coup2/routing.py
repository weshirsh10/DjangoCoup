# mysite/routing.py
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

import gameplay.routing


application = ProtocolTypeRouter({
    # (http->django views is added by default)
'websocket': AuthMiddlewareStack(
        URLRouter(
            gameplay.routing.websocket_urlpatterns
        )
    ),
})