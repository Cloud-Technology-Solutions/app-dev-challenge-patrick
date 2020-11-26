# [START imports]
import endpoints
from endpoints import remote
from protorpc import message_types
from protorpc import messages
# [END imports]

class Reponse(messages.Message):
    message = messages.StringField(1)


@endpoints.api(
    name="helloWorld",
    version='v1',
    title="Hello World API",
    description="Hello world api"
)
class HelloWorldAPI(remote.Service):
    @endpoints.method(
        message_types.VoidMessage,
        Reponse,
        path='helloWorld',
        http_method='GET',
        name='hello'
        )
    def helloWorld(self, request):
        response = Reponse()
        response.message = "HelloWorld!"
        return response


# [START api_server]
api = endpoints.api_server([HelloWorldAPI])
# [END api_server]
