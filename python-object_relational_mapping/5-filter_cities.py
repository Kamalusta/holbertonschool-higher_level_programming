#!/usr/bin/python3
""" doc """

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])
    cur = db.cursor()
    query = """SELECT cities.name FROM cities join states
on cities.state_id=states.id WHERE states.name
LIKE BINARY %s ORDER BY cities.id"""
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()
    print(', '.join(map(lambda x: x[0], rows)))
    cur.close()
    db.close()
