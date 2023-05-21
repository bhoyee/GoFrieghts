# Access to PostgreSQL Data Transfer

This script allows you to extract data from an Access database (GoFrieghts Access Database) and load it into a PostgreSQL database. It utilizes the `pyodbc` and `psycopg2` libraries to establish connections to the databases.

## Prerequisites

Before running the script, make sure you have the following components installed:

- Python 3.x
- `pyodbc` library (`pip install pyodbc`)
- `psycopg2` library (`pip install psycopg2`)
- `python-dotenv` library (`pip install python-dotenv`)

## Setup

### Download the `WPI.mdb` from 'https://drive.google.com/file/d/1VyCGCAfFuEK7vB1C9Vq8iPdgBdu-LDM4/view'
1. Place the `WPI.mdb` file in the same directory as the script (`el.py`).

2. Create a `.env` file in the same directory and provide the following environment variables:

   ```plaintext
   DB_DATABASE=<name_of_postgresql_database>
   MY_DB_USER=<postgresql_username>
   MY_DB_PASS=<postgresql_password>
   MY_DB_SERVER=<postgresql_host>
   DB_PORT=<postgresql_port>
   ```

   Replace `<name_of_postgresql_database>`, `<postgresql_username>`, `<postgresql_password>`, `<postgresql_host>`, and `<postgresql_port>` with the appropriate values.

## Usage

Run the script using the following command:

```plaintext
python main.py
```

The script will connect to the Access database, extract data from each table, create corresponding tables in the PostgreSQL database, and load the data into the respective tables.

Once the process is complete, you will see a success message indicating that the data has been loaded into PostgreSQL.

## Note

- Ensure that the necessary ODBC driver for Access is installed on your system.

- The script sanitizes the table and column names by replacing spaces and special characters with underscores.

- If you encounter any issues, verify that the file name and path for the Access database are correct, and check the environment variables in the `.env` file.

Feel free to modify the script according to your specific requirements.