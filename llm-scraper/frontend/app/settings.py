import os

from dotenv import load_dotenv

load_dotenv()

API_HOST = os.environ.get('API_HOST')
API_PORT = os.environ.get('API_PORT')
api_url = f"http://{API_HOST}:{API_PORT}/positions"