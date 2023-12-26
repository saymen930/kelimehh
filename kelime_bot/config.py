import os
 
class Config:
 
   API_ID = int(os.getenv("API_ID", "2930013"))
   API_HASH = os.getenv("API_HASH", "7cab92dcd979add511b79d693775e17d")
   BOT_TOKEN = os.getenv("BOT_TOKEN", "6803669543:AAF3IVN9OQvi0DFESZSX2Nc4W2YGFBO6__c")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "MytGrupBot")
   OWNER_ID = int(os.environ.get("OWNER_ID","1527476177"))
   OWNER_NAME = os.environ.get("OWNER_NAME", "Meyit47")
   SUPPORT = os.environ.get("SUPPORT", "S1F1RB1RCHAT")
   BOT_NAME = os.environ.get("BOT_NAME", "MytGrupBot")
