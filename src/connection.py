import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Engine


def create_connection() -> Engine:
    '''Create a database connection with a sqlalchemy engine'''
    try:
        # Create an engine instance
        engine = create_engine(_build_connection_string())
        print("Connection to PostgreSQL DB successful!!")
        return engine
    except Exception as e:
        print(f"Error: {e}")
        return None


def _build_connection_string() -> str:
    """Build the database connection string required to create an engine"""
    # Load environment variables
    load_dotenv()
    
    # Extract environment variables
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_port = int(os.getenv("DB_PORT"))
    db_name = os.getenv("DB_NAME")
    
    # Build the connection string using environment variable values
    connection_string = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    
    return connection_string


