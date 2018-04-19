'''
Created on Apr 18, 2018

@author: student
'''
from sys import argv
import csv
import numpy as np
import matplotlib as p
import pdb
from pandas import *

script, from_file = argv

# from_file = "https://pythonhow.com/data/income_data.csv"
print "Read from %s" % (from_file)

data = read_csv(from_file)
print list(data.columns.values)
print "+" * 50
print data.loc[:,"AverageHouseValue"].max()
print "+" * 50
print dir(data)
print "+" * 50
df2 = data.set_index("State", drop = False)
print df2
print "+" * 50
#print df2.loc["Alaska":"Arkansas","2005":"2007"]
#print "+" * 50
#print df2.loc[: , "2005"]
#print "+" * 50
# print df2.loc[:,"2005"].mean()
# print "+" * 50
# print df2.mean()
# data.plot()
# plt.show()


