#!/usr/bin/python3
"""
script that takes in arguments and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Accessing the database
    """
    db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    curs = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE \
            BINARY %(name)s ORDER BY states.id ASC"

    curs.execute(query, ('%' + state_name + '%',))

    states = curs.fetchall()

    for state in states:
        print(state)
