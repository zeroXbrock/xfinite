# settings.py
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")
EXPECTED_DOWN_MBPS = os.getenv("ADVERTISED_DOWN_MBPS")
EXPECTED_UP_MBPS = os.getenv("ADVERTISED_UP_MBPS")
DEBUG = os.getenv("DEBUG")
THRESHOLD_PERCENT_LOSS = os.getenv("THRESHOLD_PERCENT_LOSS")