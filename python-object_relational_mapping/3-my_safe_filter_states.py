#!/usr/bin/python3
"""
t3
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
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute the SQL query safely
    cur.execute(query, (state_name,))

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
