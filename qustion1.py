"""
Questions:
1. What are the 5 nearest ports to Singapore's JURONG ISLAND port? (country = 'SG',
port_name = 'JURONG ISLAND').Your answer should include the columns port_name and
distance_in_meters only.
"""
import os
import psycopg2
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

# Get the database credentials from environment variables
user = os.environ.get("MY_DB_USER")
password = os.environ.get("MY_DB_PASS")
host = os.environ.get("MY_DB_SERVER")
port = os.environ.get("DB_PORT")
database = os.getenv("DB_DATABASE")


# Connect to the PostgreSQL database
conn = psycopg2.connect(
    database=database,
    user=user,
    password=password,
    host=host,
    port=port
)

# Create a cursor object
cursor = conn.cursor()

# Create the table
create_table_query = """
CREATE TABLE nearest_ports (
    port_name VARCHAR(255),
    wpi_country_code VARCHAR(2),
    distance_in_meters FLOAT
);
"""
cursor.execute(create_table_query)
conn.commit()

# SQL query to get the nearest ports
query = """
INSERT INTO nearest_ports (port_name, wpi_country_code, distance_in_meters)
SELECT ji.main_port_name, ji.wpi_country_code,
       6371000 * acos(
           cos(radians(wpi.latitude_degrees::numeric) * pi() / 180) *
           cos(radians(ji.latitude_degrees::numeric) * pi() / 180) *
           cos(radians(ji.longitude_degrees::numeric) * pi() / 180 - radians(wpi.longitude_degrees::numeric) * pi() / 180) +
           sin(radians(wpi.latitude_degrees::numeric) * pi() / 180) *
           sin(radians(ji.latitude_degrees::numeric) * pi() / 180)
       ) AS distance_in_meters
FROM wpi_data wpi
JOIN wpi_data ji ON wpi.main_port_name != ji.main_port_name
WHERE wpi.main_port_name = 'JURONG ISLAND' AND wpi.wpi_country_code = 'SG' AND ji.wpi_country_code = 'SG'
ORDER BY distance_in_meters ASC
LIMIT 5;
"""

# Execute the query
cursor.execute(query)
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Table 'nearest_ports' created and data loaded successfully!")
