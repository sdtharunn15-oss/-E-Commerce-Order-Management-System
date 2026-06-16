from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./ecommerce.db"
)

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "mysecretkey"
)

ALGORITHM = os.getenv(
    "ALGORITHM",
    "HS256"
)