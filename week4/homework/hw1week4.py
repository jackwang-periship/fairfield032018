'''
Created on Apr 13, 2018

@author: student
'''
words = 'The quick brown fox jumps over the lazy dog'.split()
print words

print "*"*20
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
for i in stuff:
    print i
    
    