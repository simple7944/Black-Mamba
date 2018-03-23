from flask import Flask, Response, request
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.viber_requests import viber_request

application = Flask(__name__)




viber = Api(BotConfiguration(
    name='PythonSampleBot',
    avatar='http://media.wplm.pl/pictures/wp/photo/2012-10/414/414/hammer_and_sicklesvg.jpg',
    auth_token='47903e4860a7d433-88367fbaec064c17-feb50e42a2f20d9c'
))



@application.route("/", methods=['POST'])
def hello():

    message = viber_request.message
    # lets echo back
    viber.send_messages(viber_request.sender.id, [
        message
    ])
    return Response(status=200)

if __name__ == "__main__":
     application.run()
