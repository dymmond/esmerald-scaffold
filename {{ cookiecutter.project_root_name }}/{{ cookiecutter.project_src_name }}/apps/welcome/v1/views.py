from esmerald.permissions import DenyAll
from esmerald.responses import ORJSONResponse
from esmerald.routing.handlers import get
from esmerald.routing.views import APIView


@get(
    path="/",
    summary="Welcome API",
    description="This view is simple and shows how to use async handlers.",
)
async def welcome() -> ORJSONResponse:
    return ORJSONResponse({"message": "Welcome to your application"})


class WelcomeAPIView(APIView):
    path = "/world"

    @get(
        path="/",
        summary="Welcome from APIView",
        description="This view is simple and shows how to use async handlers inside APIView.",
    )
    async def welcome_api(self) -> ORJSONResponse:
        return ORJSONResponse({"message": "Welcome to your application using APIView"})

    @get(
        path="/deny",
        permissions=[DenyAll],
        summary="View that denies the access to everyone.",
        description="This view simply shows how to use the permissions from Esmerald.",
    )
    async def deny_access(self) -> None:
        ...
