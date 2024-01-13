#!/usr/bin/python3

"""
A script that lists all
states from the database `hbtn_0e_0_usa`
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    connect database and get all states
    """
    db_connect = MySQLdb.connect(
            host="localhost", user="argv[1]", port=3306, passwd="argv2", db="argv[3]")
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT * FROM states")
    rows_selected = db_cursor.fetchall()
    for rows in rows_selected:
        print(row)
