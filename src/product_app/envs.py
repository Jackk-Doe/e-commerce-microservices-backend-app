import os
from dotenv import load_dotenv


load_dotenv()

PORT = os.getenv('PORT')
DATABASE_URL = os.getenv('DATABASE_URL')