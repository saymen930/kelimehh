import os
 
class Config:
 
   API_ID = int(os.getenv("API_ID", "16501912"))
   API_HASH = os.getenv("API_HASH", "34138f0596a914d229f8bc1ab7794bc6")
   BOT_TOKEN = os.getenv("BOT_TOKEN", "6999080991:AAFm-Sad9EBJuGYA_y8BWLKNyHSMtBmgLeA")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "EsilaChatBot")
   OWNER_ID = int(os.environ.get("OWNER_ID","6153472412"))
   OWNER_NAME = os.environ.get("OWNER_NAME", "debubluman")
   SUPPORT = os.environ.get("SUPPORT", "sorundestekk")
   BOT_NAME = os.environ.get("BOT_NAME", "Esila Sohbet")
