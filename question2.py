"""
Questions:
2. Which country has the largest number of ports with a cargo_wharf? Your answer should
include the columns country and port_count only.
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
CREATE TABLE country_ports (
    country VARCHAR(255),
    port_count INTEGER
);
"""
cursor.execute(create_table_query)
conn.commit()

# SQL query to find the country with the largest number of ports with a cargo_wharf
query = """
INSERT INTO country_ports (country, port_count)
SELECT wpi.wpi_country_code, COUNT(*) as port_count
FROM wpi_data wpi
WHERE wpi.load_offload_wharves = 'Y'
GROUP BY wpi.wpi_country_code
ORDER BY port_count DESC
LIMIT 1;
"""

# Execute the query
cursor.execute(query)
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Table 'country_ports' created and data loaded successfully!")
