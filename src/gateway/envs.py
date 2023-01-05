import os
from dotenv import load_dotenv


load_dotenv()

PORT = os.getenv('PORT')
PRODUCT_URL = os.getenv('PRODUCT_URL')
USER_URL = os.getenv('USER_URL')