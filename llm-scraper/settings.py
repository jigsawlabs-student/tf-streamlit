import os

from dotenv import load_dotenv

load_dotenv()
open_ai_api_key = os.getenv('API_KEY')
dev_db = os.getenv('DEV_DB')
test_db = os.getenv('TEST_DB')
