
import os

from django.core.asgi import get_asgi_application
from channels.routing import URLRouter,ProtocolTypeRouter
import api.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_chat_app.settings')

application = ProtocolTypeRouter(
    {
        'http':get_asgi_application(),
        'websocket':URLRouter(
            api.routing.websocket_patterns
        )
    }
)
