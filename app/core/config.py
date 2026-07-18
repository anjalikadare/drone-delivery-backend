import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "insecure_default")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./drone_delivery.db")
