# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "29219170"))
API_HASH = os.environ.get("API_HASH", "12d6648ede66e1ef31d9c455317ee09d")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6083104743:AAGGTiP7q5uLzbB6EQo9dZyZtWRNYSYgFZ0")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("5897793065")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Shortner")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Sohanrazz:Sohanrazz@cluster0.wlnnp18.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5897793065")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(5897793065)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-984281737")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Netflix_Hindi_Movies_4k2") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
