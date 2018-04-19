'''
Created on Apr 18, 2018

@author: student
'''
from sys import argv
import csv

script, from_file, to_file, word_to_search = argv

print "Read from %s to %s" % (from_file, to_file)

in_file = open(from_file, 'rb')
out_file = open(to_file, 'wb')
i = 0
try:
#     reader = csv.DictReader(in_file)
    reader = csv.reader(in_file)
    writer = csv.writer(out_file)
    for row in reader:
        if i == 0 or i % 5 == True:
            writer.writerow(row)
        i = i + 1    
finally:
    in_file.close()
    out_file.close()

print "Alright, all done: Total of %d lines were picked up" % i
