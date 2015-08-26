#!/usr/bin/python
#coding:utf-8
import string
import sqlite3, sys
import random

conn=sqlite3.connect('data.db')
curs = conn.cursor()
curs.execute('''
    CREATE TABLE sentences (
    id  TEXT  PRIMARY KEY,
    content TEXT
    );
    ''')

conn.commit()
conn.close()