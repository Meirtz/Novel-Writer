#!/usr/bin/python
#coding:utf-8
import string
import sqlite3, sys
import random
import jieba
import jieba.analyse

def check(str):
    line = "".join(str.split('。|，|,|\n|.'))

    if (line.find('com') == -1 and line.startswith('第') == 0 and line.startswith('\n') == 0 and line.startswith('\r') == 0 ):
        return 1
    else:
        return 0


will_cal_tags = input("Would you like to replace the tags with members in dict.txt: (Y/n)")


rf = open(r'tdata.txt')
resf = open('result.txt', 'w')

conn=sqlite3.connect('ata.db')
curs = conn.cursor()

table_del = 'DROP TABLE IF EXISTS sentences'
curs.execute(table_del)



curs.execute('''
    CREATE TABLE sentences (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content VARCHAR(1024)
    );
    ''')

query = 'INSERT INTO sentences VALUES (?,?)'

data = [line.split('。|，|,|\n|.') for line in rf.readlines() if check(line)]
max = 0
for i in range(len(data)):
    #print( "%s" % ("".join(data[i]).strip()),file=of)
    vals = (i,("".join(data[i]).strip()))
    curs.execute(query,vals)
    max = i

query = 'SLECT'
for i in range(999):
    index = random.randint(5,max)
    curs.execute('''SELECT content FROM sentences WHERE id == (%d);''' % index)
    for row in curs:
        flag = random.randint(1,7)
        print('%s' % row,end='',file=resf)
        if (flag == 1):print('\n',file=resf)

conn.commit()
conn.close()
rf.close()

if (will_cal_tags == 'Y'):
    content = open('result.txt', 'rb').read()
    tags = jieba.analyse.extract_tags(content, topK=10)
    print(",".join(tags))

    re_dict = open(r'dict.txt')
    data_d = [line for line in re_dict.readlines()]

    re_ex = open('result_ex.txt','w')
    lines = open('result.txt', 'rb').readlines()
    #data_res = [line.replace(tags[0],data_d[0]) for line in resf.readlines()]
    for s in lines:
        s0 = tags[0]
        re_ex.seek(0)
        re_ex.truncate()
        #print('%s',s.replace(tags[0],data_d[0])).encode()



