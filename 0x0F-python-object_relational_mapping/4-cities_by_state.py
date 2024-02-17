#!/usr/bin/python3
"""
 script that lists all cities from the database hbtn_0e_4_usa
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

    query = "SELECT cities.id, cities.name, states.name \
        FROM cities JOIN states ON cities.state_id \
            = states.id ORDER BY cities.id ASC"
    curs.execute(query)

    states = curs.fetchall()

    for state in states:
        print(state)
