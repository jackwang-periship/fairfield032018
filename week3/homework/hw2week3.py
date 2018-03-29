'''
Created on Mar 29, 2018

@author: student
'''
import os

f = open('TEST', 'r')
f.seek(0, os.SEEK_END)
file_size = f.tell()
print "The total size of the file is: %d" % file_size
f.seek(0)
print "19 characters have being read: %s" % f.read(19)
current_pos = f.tell()  # get to know the current position in the file
print "This current postion of the file is: %d" % current_pos
current_pos = current_pos + 6 
f.seek(current_pos)
print "Another 5 characters have being read from file: %s" % f.read(5)
f.seek(0)
print "Print the entire file with line break and return an array!"
print f.readlines()
f.close()