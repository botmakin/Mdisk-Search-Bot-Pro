import os
# from dotenv import load_dotenv

# load_dotenv()


class Config(object):
    API_ID = int(os.getenv("API_ID", 15823382))
    API_HASH = os.getenv("API_HASH", "016d5e115a06ddfb6121823d72ae4d8c")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.getenv("BOT_SESSION_NAME", "MdiskSearcbot")
    USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
    BOT_USERNAME = os.getenv("BOT_USERNAME", "Mdisk_search_re_bot")
    BOT_OWNER = int(os.getenv("BOT_OWNER", "5921087216"))
#    OWNER_USERNAME = os.getenv("OWNER_USERNAME", "Ipapcorn_helper")
    BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL", "ipapcornsupport")
#    GROUP_USERNAME = os.getenv("GROUP_USERNAME", "ipapcornsupport")
    START_MSG = os.getenv("START_MSG", ''' ''')
    START_PHOTO = os.getenv("START_PHOTO", "https://telegra.ph/file/3073c7543fc3ab93659d9.jpg")
    HOME_TEXT = os.getenv("HOME_TEXT", ''' ''')
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", -1001740189478)
    DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://W9Uyj61afEXSw601:W9Uyj61afEXSw601@cluster0.zsxso.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1001670571048"))
    RESULTS_COUNT = int(os.getenv("RESULTS_COUNT", 25))
    BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "False")
    UPDATES_CHANNEL_USERNAME = os.getenv("UPDATES_CHANNEL_USERNAME", "Film_Update_Official")
    FORCE_SUB = os.getenv("FORCE_SUB", "True")
    AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", 0))
    MDISK_API = os.getenv("MDISK_API", "XXgy4PoF35VECI7kZgTb")
    VERIFIED_TIME  = int(os.getenv("VERIFIED_TIME", "31"))
    ABOUT_BOT_TEXT = os.getenv("ABOUT_TEXT", ''' ''')
    ABOUT_HELP_TEXT = os.getenv("HELP_TEXT", ''' ''')
