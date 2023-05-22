"""
Question 3: You receive a distress call from the middle of the North Atlantic Ocean. The person on the
line gave you a coordinates of lat: 32.610982, long: -38.706256 and asked for the nearest port
with provisions, water, fuel_oil and diesel. Your answer should include the columns country,
port_name, port_latitude and port_longitude only.
"""

import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the PostgreSQL connection details from environment variables
db_host = os.environ.get("MY_DB_SERVER")
db_port = os.environ.get("DB_PORT")
db_name = os.getenv("DB_DATABASE")
db_user = os.environ.get("MY_DB_USER")
db_password = os.environ.get("MY_DB_PASS")

# SQL query
sql_query = """
    SELECT main_port_name, wpi_country_code, latitude_degrees, longitude_degrees,
        2 * 6371 * asin(sqrt(
            sin(radians(latitude_degrees::numeric - 32.610982) / 2) ^ 2 +
            cos(radians(32.610982)) * cos(radians(latitude_degrees::numeric)) *
            sin(radians(longitude_degrees::numeric - (-38.706256)) / 2) ^ 2
        )) AS distance
    FROM wpi_data
    WHERE supplies_provisions = 'Y' AND supplies_water = 'Y' AND supplies_fuel_oil = 'Y' AND supplies_diesel_oil = 'Y'
    ORDER BY distance ASC
    LIMIT 1;
"""

# PostgreSQL connection
conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    dbname=db_name,
    user=db_user,
    password=db_password
)

# Create a cursor object
cursor = conn.cursor()

# Create the table in PostgreSQL
create_table_query = """
    CREATE TABLE nearest_port (
        main_port_name VARCHAR(255),
        wpi_country_code VARCHAR(255),
        latitude_degrees FLOAT,
        longitude_degrees FLOAT,
        distance FLOAT
    );
"""
cursor.execute(create_table_query)
print("Table created successfully.")

# Execute the SQL query and insert the result into the table
cursor.execute(sql_query)
result = cursor.fetchone()

# Insert the result into the table
insert_query = """
    INSERT INTO nearest_port (main_port_name, wpi_country_code, latitude_degrees, longitude_degrees, distance)
    VALUES (%s, %s, %s, %s, %s);
"""
cursor.execute(insert_query, result)
conn.commit()
print("Data inserted successfully.")

# Close the cursor and connection
cursor.close()
conn.close()
