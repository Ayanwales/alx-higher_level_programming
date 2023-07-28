#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
                INNER JOIN states ON state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC;", (sys.argv[4],))

    rows = cur.fetchall()
    i = 1
    for r in rows:
        if i < len(rows):
            print("{:s}, ".format(r[0]), end="")
            i += 1
        else:
            print(r[0], end="")
    print()
    cur.close()
    db.close()
