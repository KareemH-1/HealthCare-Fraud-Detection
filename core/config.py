import os
import urllib.parse
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DB_SERVER = os.getenv("DB_SERVER")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PWD = os.getenv("DB_PWD")
    DB_DRIVER = os.getenv("DB_DRIVER")

    connection_string = (
        f"Driver={DB_DRIVER};"
        f"Server=tcp:{DB_SERVER},1433;"
        f"Database={DB_NAME};"
        f"Uid={DB_USER};"
        f"Pwd={DB_PWD};"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
        "Connection Timeout=30;"
    )
    params = urllib.parse.quote_plus(connection_string)
    DATABASE_URL = f"mssql+pyodbc:///?odbc_connect={params}"

    KAFKA_BOOTSTRAP_SERVERS: str = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
    KAFKA_TOPIC: str = os.getenv("TOPIC_CLAIMS_RAW", "healthcare-claims")
    KAFKA_CONSUMER_GROUP: str = os.getenv("KAFKA_CONSUMER_GROUP", "fraud-detection-group")
    EVENTHUB_CONNECTION_STRING: str = os.getenv("EVENTHUB_CONNECTION_STRING", "")

    APP_BASE_URL: str = os.getenv("APP_BASE_URL", "http://localhost:8000")


settings = Settings()
