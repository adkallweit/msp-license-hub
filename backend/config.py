import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    SOPHOS_CLIENT_ID = os.getenv("SOPHOS_CLIENT_ID")
    SOPHOS_SECRET = os.getenv("SOPHOS_SECRET")

    VEEAM_URL = os.getenv("VEEAM_URL")
    VEEAM_TOKEN = os.getenv("VEEAM_TOKEN")

    CENTRON_URL = os.getenv("CENTRON_URL")
    CENTRON_USER = os.getenv("CENTRON_USER")
    CENTRON_PASS = os.getenv("CENTRON_PASS")

    DATABASE_URL = os.getenv("DATABASE_URL")
