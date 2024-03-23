#!/usr/bin/python3
"""
this script retrive data which starting with 'N'
form a database with MySQLdb modul
"""


import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states ORDER BY states.id ASC"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        if row[1].startswith("N"):
            print(row)
    cur.close()
    db.close()
