#!/usr/bin/python3
"""
script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
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

    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY \
        states.id ASC".format(argv[4])
    curs.execute(query)

    states = curs.fetchall()

    for state in states:
        print(state)
