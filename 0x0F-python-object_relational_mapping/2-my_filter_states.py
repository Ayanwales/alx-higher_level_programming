#!/usr/bin/python3
"""print name and id for given name for a table using MySQLdb"""
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT id,\
                name FROM states WHERE name = '{}'\
                ORDER BY id ASC".format(sys.argv[4]))

    rows = cur.fetchall()
    for r in rows:
        if r[1] == sys.argv[4]:
            print(r)
