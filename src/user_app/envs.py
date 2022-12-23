import os
from dotenv import load_dotenv


load_dotenv()

# This app Port value
PORT = os.getenv('PORT')

# Database Url
DATABASE_URL = os.getenv('DATABASE_URL')

# Application mode (e.g. dev, deploy, test). Default is set to dev mode
MODE = os.getenv('MODE', 'dev')