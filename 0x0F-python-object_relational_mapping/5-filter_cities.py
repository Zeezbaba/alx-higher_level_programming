#!/usr/bin/python3
"""
 script that takes in the name of a state as an argument and lists all
 cities of that state, using the database hbtn_0e_4_usa
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

    query = "SELECT cities.id, cities.name FROM cities \
        JOIN states ON cities.state_id = states.id \
            WHERE states.name LIKE BINARY %(state_name)s \
                ORDER BY cities.id ASC"
    curs.execute(query, {'state_name': argv[4]})

    cities = curs.fetchall()

    if cities is not None:
        print(", ".join([city[1] for city in cities]))
