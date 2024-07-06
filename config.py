import os

# Telegram Bot Configuration
API_ID = int(os.getenv('AAHfiqksKZ8WmR2zSjiQ7_v4TMAKdiHm9T0', ''))
API_HASH = os.getenv('270485614', '')
BOT_TOKEN = os.getenv('7215728836:AAGiuVJ-zmHBSqjkathnizbcZueOXSuMIWc', '')
BOT_NAME = os.getenv('MEERA AI', '')
BOT_USERNAME = os.getenv('@meeraai_bot', '')
OWNER_ID = int(os.getenv('OWNER_ID', ''))
OWNER_USERNAME = os.getenv('OWNER_USERNAME', '')
UPDATE_CHANNEL = os.getenv('UPDATE_CHANNEL', '')
SUPPORT_GROUP = os.getenv('SUPPORT_GROUP', '')

# OpenAI Configuration
OPENAI_KEY = os.getenv('OPENAI_KEY', '')

# MongoDB Configuration
MONGODB_URL = os.getenv('MONGODB_URL', '')

# Check if all required environment variables are set
if not all([API_ID, API_HASH, BOT_TOKEN, OPENAI_KEY, OWNER_ID, OWNER_USERNAME, UPDATE_CHANNEL, SUPPORT_GROUP, MONGODB_URL]):
    raise RuntimeError("Please set all required environment variables: API_ID, API_HASH, BOT_TOKEN, OPENAI_KEY, OWNER_ID, OWNER_USERNAME, UPDATE_CHANNEL, SUPPORT_GROUP, MONGODB_URL")
