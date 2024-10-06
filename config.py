import os
import logging

API_ID = 23981002

API_HASH = os.environ.get("API_HASH", "9549825af7363be26b4b53e5bb3e737a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7521089253:AAGHqiw4e7ewdc1qt7eonChimNf-Dr7dYXw")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", "6348445990"))

# Setting up logging
LOG = logging.getLogger("my_logger")
LOG.setLevel(logging.INFO)
handler = logging.StreamHandler()  # Outputs logs to console
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
LOG.addHandler(handler)

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6348445990").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
