import os

from dotenv import load_dotenv

load_dotenv()


username = os.environ.get('DB_USERNAME')
password = os.environ.get('DB_PASSWORD')
host = os.environ.get('DB_HOST')
database = os.environ.get('DB_NAME')
db_conn = f'postgresql://{username}:{password}@{host}/{database}'
