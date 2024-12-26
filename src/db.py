from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import psycopg2

def create_connection():
    try:
        # Create an engine instance
        engine = create_engine(
            "postgresql+psycopg2://postgres:postgres@localhost:5433/postgres"
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