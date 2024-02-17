#!/usr/bin/python3
"""
script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Accessing the database
    """
    db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    curs = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE \
            BINARY 'N%' ORDER BY states.id ASC"
    curs.execute(query)

    states = curs.fetchall()

    for state in states:
        print(state)
