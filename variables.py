# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX


class Config(object):
    # Configuration class for the bot

    # Enable or disable logging
    LOGGER = True

    # <================================================ REQUIRED ======================================================>
    # Telegram API configuration
    API_ID = "22920902"  # Get this value from my.telegram.org/apps
    API_HASH = "9b6416fcccd2b728f1661877ca9a14cf"

    # Database configuration (PostgreSQL)
    DATABASE_URL = "postgresql://raidenistriku_owner:W2s8DraLEFvt@ep-quiet-truth-a4d6kmc9.us-east-1.aws.neon.tech/raidenistriku"

    # Event logs chat ID and message dump chat ID
    EVENT_LOGS = "-1002095596112"
    MESSAGE_DUMP = "-1002095596112"

    # MongoDB configuration
    MONGO_DB_URI = "mongodb+srv://Nonalcoholic:8eVPSTcJa2c3FkH@cluster0.bprf1b2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    # Support chat and support ID
    SUPPORT_CHAT = "gcsupport_Ryo_bot_id"
    SUPPORT_ID = "-1002095596112"

    # Database name
    DB_NAME = "MikoDB"

    # Bot token
    TOKEN = "7125789785:AAGfwpkCD5ZVTmHfr9XJ3pQmhNfpZBFGhCk"  # Get bot token from @BotFather on Telegram

    # Owner's Telegram user ID (Must be an integer)
    OWNER_ID = "6995317382"
    # <=======================================================================================================>

    # <================================================ OPTIONAL ======================================================>
    # Optional configuration fields

    # List of groups to blacklist
    BL_CHATS = []

    # User IDs of sudo users, dev users, support users, tiger users, and whitelist users
    DRAGONS = [5965193875, 6979724550, 6071124527]  # Sudo users
    DEV_USERS = [6995317382]  # Dev users
    DEMONS = [6995317382]  # Support users
    TIGERS = []  # Tiger users
    WOLVES = []  # Whitelist users

    # Toggle features
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True

    # Modules to load or exclude
    LOAD = []
    NO_LOAD = []

    # Global ban settings
    STRICT_GBAN = True

    # Temporary download directory
    TEMP_DOWNLOAD_DIRECTORY = "./"
    # <=======================================================================================================>


# <=======================================================================================================>


class Production(Config):
    # Production configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True


class Development(Config):
    # Development configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True
