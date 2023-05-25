# Microsoft Access to PostgreSQL Data Transfer

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


## Additional Queries

1. **What are the 5 nearest ports to Singapore's JURONG ISLAND port?**

To find the 5 nearest ports to Singapore's JURONG ISLAND port, you can execute a SQL query in your PostgreSQL database. The query should include the columns `port_name` and `distance_in_meters` to provide the desired answer. You can modify the query to use the appropriate table and column names for your database schema.

2. **Which country has the largest number of ports with a cargo_wharf?**

To determine the country with the largest number of ports with a cargo_wharf, you can execute a SQL query in your PostgreSQL database. The query should include the columns `country` and `port_count` to provide the desired answer. Again, modify the query to match your specific table and column names.

3. **You receive a distress call from the middle of the North Atlantic Ocean. The person on the line gave you coordinates of latitude 32.610982 and longitude -38.706256. They asked for the nearest port with provisions, water, fuel_oil, and diesel.**

To find the nearest port with the required provisions and amenities, you can execute a SQL query in your PostgreSQL database. The query should include the columns `country`, `port_name`, `port_latitude`, and `port_longitude` to provide the necessary information. Adjust the query to fit your table and column names.

Feel free to modify the script and SQL queries according to your specific requirements and database schema.
