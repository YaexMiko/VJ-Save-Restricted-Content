import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "27238809"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "c854867f7b27f65aebd41392eb2af1d9")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://ZeroTwo:aloksingh@zerotwo.3q3ij.mongodb.net/?retryWrites=true&w=majority")
