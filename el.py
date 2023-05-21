import pyodbc
import psycopg2
import os
import glob
import re
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def extract_data_from_access(access_file_path):
    # Connect to the Access database
    access_conn_str = r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + access_file_path + ";"
    access_conn = pyodbc.connect(access_conn_str)
    access_cursor = access_conn.cursor()

    # Get the table names in the Access database
    table_names = access_cursor.tables(tableType='TABLE')
    access_table_names = [table.table_name for table in table_names]

    data = {}
    # Fetch data from each Access table
    for access_table_name in access_table_names:
        # Fetch data from Access table
        access_cursor.execute(f"SELECT * FROM [{access_table_name}]")
        access_columns = [column[0].lower().replace(" ", "_") for column in access_cursor.description]
        access_rows = access_cursor.fetchall()

        data[access_table_name] = {
            'columns': access_columns,
            'rows': access_rows
        }

    # Close the Access connection
    access_cursor.close()
    access_conn.close()

    return data


def load_data_to_postgresql(data, database, user, password, host, port):
    # Connect to the PostgreSQL database
    pgsql_conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
    pgsql_cursor = pgsql_conn.cursor()

    # Iterate over the data and load it into PostgreSQL
    for access_table_name, table_data in data.items():
        # Sanitize table name
        pgsql_table_name = re.sub(r'\W+', '_', access_table_name.lower())

        # Create the table in PostgreSQL
        column_definitions = ", ".join(['"' + re.sub(r"\W+", "_", col.lower()) + '" text' for col in table_data['columns']])
        create_table_query = 'CREATE TABLE IF NOT EXISTS "{}" ({})'.format(pgsql_table_name, column_definitions)
        pgsql_cursor.execute(create_table_query)
        pgsql_conn.commit()

        # Insert data into the table
        for access_row in table_data['rows']:
            insert_query = 'INSERT INTO "{}" ({}) VALUES ({})'.format(
                pgsql_table_name,
                ", ".join(['"' + re.sub(r"\W+", "_", col.lower()) + '"' for col in table_data['columns']]),
                ", ".join(["%s"] * len(table_data['columns']))
            )
            pgsql_cursor.execute(insert_query, access_row)

        pgsql_conn.commit()

    # Print success message
    print("Data loaded into PostgreSQL successfully!")

    # Close the PostgreSQL connection
    pgsql_cursor.close()
    pgsql_conn.close()
