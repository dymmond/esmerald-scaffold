from esmerald.routing.gateways import Gateway

from .views import WelcomeAPIView, welcome

route_patterns = [
    Gateway(path="/welcome", handler=welcome, name="welcome"),
    Gateway(path="/welcome-apiview", handler=WelcomeAPIView, name="welcome-apiview"),
]
