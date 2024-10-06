import os

API_ID = API_ID =  23981002

API_HASH = os.environ.get("API_HASH", "9549825af7363be26b4b53e5bb3e737a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7521089253:AAGHqiw4e7ewdc1qt7eonChimNf-Dr7dYXw")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", "6348445990" ))

LOG = ,

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6348445990").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


