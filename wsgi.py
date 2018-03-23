from flask import Flask, Response
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration


application = Flask(__name__)

viber = Api(BotConfiguration(
    name='PythonSampleBot',
    avatar='http://media.wplm.pl/pictures/wp/photo/2012-10/414/414/hammer_and_sicklesvg.jpg',
    auth_token='47903e4860a7d433-88367fbaec064c17-feb50e42a2f20d9c'
))

# viber.set_webhook('https://black-mamba-black-mamba.1d35.starter-us-east-1.openshiftapps.com:8080/')

@application.route("/")
def hello():

    return Response(status=200)

if __name__ == "__main__":
     application.run()
