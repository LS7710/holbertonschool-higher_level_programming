#!/usr/bin/python3
"""
t5
"""


import sys
import MySQLdb


def main():
    # Unpack command line arguments
    mysql_username, mysql_password, database_name, state_name = sys.argv[1:]

    # Establish a database connection
    db = MySQLdb.connect(host="localhost",
                         user=mysql_username,
                         passwd=mysql_password,
                         db=database_name,
                         port=3306)

    # Create a cursor object
    cur = db.cursor()

    # Create the SQL query string using parameterized queries
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    # Execute the SQL query
    cur.execute(query, (state_name,))

    # Fetch all the rows
    rows = cur.fetchall()

    # Process and print the city names as a comma-separated string
    if rows:
        print(', '.join(city[0] for city in rows))
    else:
        print()

    # Close cursor and database connection
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
