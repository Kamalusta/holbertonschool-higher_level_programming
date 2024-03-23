#!/usr/bin/python3
''' doc '''
import MySQLdb
import sys


db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                     password=sys.argv[2], db=sys.argv[3])
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
db.close()
