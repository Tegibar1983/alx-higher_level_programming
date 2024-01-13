#!/usr/bin/python3
"""
This scrips will list all state
found in 'hbtn_0e_0_usa'
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """ Acess the database and get all the states
    inside it;
    """
    db_connect = MySQLdb.connect(
            host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()
    db_cursor.execute('SELECT * FROM states')
    rows_selected = db_cursor.fetchall()
    for row in rows_selected:
        print(row)

