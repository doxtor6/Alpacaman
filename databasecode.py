# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 23:04:19 2023

@author: timmy
"""

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS data (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user TEXT NOT NULL,
                            time TEXT NOT NULL,
                            content TEXT NOT NULL
                          );""")
    except Error as e:
        print(e)

def insert_data(conn, data):
    try:
        sql = '''INSERT INTO data(user, time, content) VALUES (?, ?, ?);'''
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(e)

def savedanmu(datalist):
    database = "data.db"
    conn = create_connection(database)
    if conn is not None:
        create_table(conn)
        # 示例数据
        for d in datalist:
            data_id = insert_data(conn, d)
        conn.close()
    else:
        print("Error! Cannot create the database connection.")
        
def readdamu(n):
    database = "data.db"
    conn = create_connection(database)
    if conn is not None:
        create_table(conn)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM data ORDER BY id DESC LIMIT "+str(n))
        rows = cursor.fetchall()
        conn.close()
        return rows
    else:
        print("Error! Cannot create the database connection.")

def deletelastdanmu():
    database = "data.db"
    conn = create_connection(database)
    if conn is not None:
        create_table(conn)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM data WHERE id = (SELECT MAX(id) FROM data)")
        conn.commit()
        conn.close()
    else:
        print("Error! Cannot create the database connection.")

def readuser(username,n):
    database = "data.db"
    conn = create_connection(database)
    if conn is not None:
        create_table(conn)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM data WHERE user = '"+username+"' ORDER BY id DESC LIMIT "+str(n))
        rows = cursor.fetchall()
        conn.close()
        return rows
    else:
        print("Error! Cannot create the database connection.")

