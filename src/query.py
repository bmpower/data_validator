from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from connection import create_connection


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


if __name__ == "__main__":
    engine = create_connection()
    if engine:
        query_database(engine)