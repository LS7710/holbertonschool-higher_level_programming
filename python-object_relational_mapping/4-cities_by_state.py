#!/usr/bin/python3
"""
t4
"""

import sys
import MySQLdb


def main():
    # Unpack command line arguments
    mysql_username, mysql_password, database_name = sys.argv[1:]

    # Establish a database connection
    db = MySQLdb.connect(host="localhost",
                         user=mysql_username,
                         passwd=mysql_password,
                         db=database_name,
                         port=3306)

    # Create a cursor object
    cur = db.cursor()

    # Create the SQL query string
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """

    # Execute the SQL query
    cur.execute(query)

    # Fetch all the rows
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
