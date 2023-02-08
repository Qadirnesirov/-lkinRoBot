# Create a new config.py or rename this to config.py file in same dir and import, then extend this class. okey.
import json
import os


sudos = 1801589805
devs = 1801589805
supports = 1801589805
whitelists = 1801589805
tigers = 1801589805
spammers = 1801589805


def get_user_list(config, key):
    with open('{}/SaitamaRobot/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    #Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 26712413  # integer value, dont use ""
    API_HASH = "3298034eb7cec614ef852fda02536153"
    TOKEN = "6065065057:AAF1bXLnFnq5c9Rqy3Z_5RpUgLWBzeyITBs"  #This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1727079853  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "nesirovqadirofficiall"
    SUPPORT_CHAT = 'sevgimsende'  #Your own group for support, do not add the @
    JOIN_LOGGER = -1001842770743  #Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = -1001842770743  #Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    #RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:631T2dGYEfANXb0sORrY@containers-us-west-14.railway.app:6631/railway'  # needed for any database modules
    LOAD = []
    NO_LOAD = ['rss', 'cleaner', 'connection', 'math']
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@imperatorofficiall"

    #OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = ('sudos')
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = ('devs')
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = ('supports')
    #List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = ('tigers')
    WOLVES = ('whitelists')
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  #Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. Set as number of threads your processor uses
    BAN_STICKER = 'CAACAgQAAx0CU_rCTAABAczQXyBOv1TsVK4EfwnkCUT1H0GCkPQAAtwAAwEgTQaYsMtAltpEwhoE'  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = 'awoo'  # Get your API key from https://www.alphavantage.co/support/#api-key
    TIME_API_KEY = 'awoo'  # Get your API key from https://timezonedb.com/api
    WALL_API = 'awoo'  #For wallpapers, get one from https://wall.alphacoders.com/api.php
    AI_API_KEY = 'awoo'  #For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    ALLOW_CHATS = None

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
