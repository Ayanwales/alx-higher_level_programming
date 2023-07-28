#!/usr/bin/python3
"""script to print name starting with N form a table using MySQLdb"""
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT states.id,\
                states.name FROM states WHERE name LIKE BINARY 'N%'\
                ORDER BY states.id ASC")
    rows = cur.fetchall()
    for r in rows:
        print(r)
