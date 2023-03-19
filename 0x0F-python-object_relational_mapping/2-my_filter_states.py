#!/usr/bin/python3
"""
The script that takes in an argument and displays it in
the state table of the database where the name matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
conn = mysql.connect(host="localhost", user=argv[1], password=argv[2]
     , db=argv[3], port=3306)
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    kudus = cursior.db()
    kudus.execute("SELECT * FROM states \
            WHERE name LIKE BINARY 'N%'\
            ORDER BY states.id ASC")
    rows = kudus.fetchall()

    for row in rows:
        print(row)
