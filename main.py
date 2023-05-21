import pyodbc
import psycopg2
import os
import glob
import re
from dotenv import load_dotenv
from el import extract_data_from_access, load_data_to_postgresql

load_dotenv()  # Load environment variables from .env file


def main():
    access_file_path = os.path.abspath("WPI.mdb")
    database = os.environ.get("DB_DATABASE")
    user = os.environ.get("MY_DB_USER")
    password = os.environ.get("MY_DB_PASS")
    host = os.environ.get("MY_DB_SERVER")
    port = os.environ.get("DB_PORT")

    # Extract data from Access
    data = extract_data_from_access(access_file_path)

    # Load data into PostgreSQL
    load_data_to_postgresql(data, database, user, password, host, port)

# Execute the main function
if __name__ == "__main__":
    main()