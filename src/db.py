import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def create_connection():
    try:
        # Retrieve database credentials from environment variables
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_host = os.getenv("DB_HOST")
        db_port = os.getenv("DB_PORT")
        db_name = os.getenv("DB_NAME")

        # Create an engine instance
        engine = create_engine(
            f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{int(db_port)}/{db_name}"
        )
        print("Connection to PostgreSQL DB successful")
        return engine
    except Exception as e:
        print(f"Error: {e}")
        return None

def query_database(engine):
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()

    try:
        # Example query
        result = session.execute(text("SELECT * FROM USERS"))
        for row in result:
            print(row)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        session.close()

# Example usage
if __name__ == "__main__":
    engine = create_connection()
    if engine:
        query_database(engine)