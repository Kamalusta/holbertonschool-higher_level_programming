#!/usr/bin/python3
"""
this script retrive data which name is in argument
form a database with MySQLdb modul
"""


import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY \'{}\' ORDER BY id ASC"
    cur.execute(query.format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
