import os
from dotenv import load_dotenv
load_dotenv()

SOURCE_DB_URL = os.getenv("SOURCE_DB_URL")
AZURE_CONN_STRING = os.getenv("AZURE_CONN_STRING")
AZURE_CONTAINER_NAME = os.getenv("AZURE_CONTAINER_NAME")
