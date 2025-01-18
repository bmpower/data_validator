import os
from dotenv import load_dotenv


def build_connection_string():
    """Build the database connection string required to create an engine"""
    connection_info = _get_connection_info()

    # Build the connection string using values from connection_info dict
    connection_string = f"postgresql+psycopg2://{connection_info['db_user']}:"
    connection_string += f"{connection_info['db_password']}@{connection_info['db_host']}:"
    connection_string += f"{int(connection_info['db_port'])}/{connection_info['db_name']}"
    
    return connection_string


def _get_connection_info():
    """Load and retrieve the environment variables for database connection"""
    # Load environment variables
    load_dotenv()
    
    # Retrieve database credentials from environment variables
    connection_string_params = ['db_user', 
                                'db_password', 
                                'db_host', 
                                'db_port', 
                                'db_name',
                                ]
    connection_info = {}
    for param in connection_string_params:
        arg = os.getenv(f"{param.upper()}")
        connection_info.update({param: arg})
    return connection_info



   
    



