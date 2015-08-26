#!/usr/bin/python
#coding:utf-8
import string
import random


rf = open(r'tdata.txt')
of = open('data.txt', 'w')
resf = open('result.txt', 'w')



data = [line.split('。|，|,|\n|.') for line in rf.readlines() if "".join(line.split('。|，|,|\n|.')).find("77nt") == -1]
max = 0
for i in range(len(data)):
    print( "%s" % ("".join(data[i]).strip()),file=of)
    max = i
rf.close()
data = [line.split('。|，|,|\n|.') for line in rf.readlines() if "".join(line.split('。|，|,|\n|.')).find("77nt") == -1]
of.close()


for i in range(999):
    index = random.randint(5,max)
    flag = random.randint(1,7)
    print( "%s" % ("".join(data[index]).strip()),file=resf,end=''),
    if (flag == 1):print('\n',file=resf)
