'''
Created on Mar 29, 2018

@author: student
'''
from sys import argv

script, filenameTOBEconcatenated, filenameTOBEreadfrom = argv

fd = open(filenameTOBEconcatenated, 'a')
fr = open(filenameTOBEreadfrom, 'r')

# Read the file that contains the contents of which we want to take and append to the file
# named filenameTOBEconcatenated
filecontent = fr.read()
fr.close()
# Write/Append the filecontent to filenameTOBEconcatenated
fd.write(filecontent)
fd.close()

fd = open(filenameTOBEconcatenated, 'r')
contents = fd.read()
print contents