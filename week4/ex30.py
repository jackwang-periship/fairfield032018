'''
Created on Apr 7, 2018

@author: Student
'''
people = 30
cars = 40
buses = 15


if cars > people:
    print "We should take the cars."
    
    if buses > 10:
        print "\tThis is a nested If"
    
elif cars < people:
    print "We should not take the cars."
    print "We should take the cars."
    print "We should take the cars."
    print "We should take the cars."
    print "We should take the cars."

elif cars < people:
    print "We should not take the cars."
    print "We should take the cars."
    print "We should take the cars."
    print "We should take the cars."
    print "We should take the cars."

else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."