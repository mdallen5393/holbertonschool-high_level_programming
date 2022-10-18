#!/usr/bin/python3
# This script lists all `states` from the database
# `hbtn_0e_0_usa`.

import MySQLdb
import sys

db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()

cur.execute("SELECT * FROM states ORDER BY id")
results = cur.fetchall()
for row in results:
    print(row)
