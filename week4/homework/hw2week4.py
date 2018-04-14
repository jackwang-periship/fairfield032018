'''
Created on Apr 13, 2018

@author: student
'''
"""
isinstance(i, int)
isinstance(f, float)
isinstance(s, str)
isinstance(l, list)
isinstance(d, dict)
isinstance(t, tuple)
"""

myList = ["Hello", 1, "World!", 345, "My height", 5.11]
#myList = ["Hello", 1, "World!", 345, "My height", 5.11, ["Avtech", "Fairfield"]]

for i in myList:
    if isinstance(i, int):
        print("%d") % i
    elif isinstance(i, str):
        print("%s") % i
    elif isinstance(i, float):
        print("%f") % i
    else:
        print("%r") % i

