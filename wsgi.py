from flask import Flask, Response, request
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import VideoMessage
from viberbot.api.messages.text_message import TextMessage
import logging

from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest

application = Flask(__name__)




viber = Api(BotConfiguration(
    name='PythonSampleBot',
    avatar='http://media.wplm.pl/pictures/wp/photo/2012-10/414/414/hammer_and_sicklesvg.jpg',
    auth_token='47903e4860a7d433-88367fbaec064c17-feb50e42a2f20d9c'
))



@application.route("/", methods=['POST'])
def hello():
    # logger.debug("received request. post data: {0}".format(request.get_data()))
    # every viber message is signed, you can verify the signature using this method
    if not viber.verify_signature(request.get_data(), request.headers.get('X-Viber-Content-Signature')):
        return Response(status=403)

    # this library supplies a simple way to receive a request object
    viber_request = viber.parse_request(request.get_data())

    if isinstance(viber_request, ViberMessageRequest):
        message = viber_request.message
        # lets echo back
        viber.send_messages(viber_request.sender.id, [
            message
        ])
    elif isinstance(viber_request, ViberSubscribedRequest):
        viber.send_messages(viber_request.get_user.id, [
            TextMessage(text="thanks for subscribing!")
        ])
    
        # logger.warn("client failed receiving message. failure: {0}".format(viber_request))

    return Response(status=200)

if __name__ == "__main__":
     application.run()
