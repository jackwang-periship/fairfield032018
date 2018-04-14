'''
Created on Apr 13, 2018

@author: student
'''
#First we define the dictionary
#it will have nothing in it this time

#We can do the following:
"""
    ages = { 'Sue' : 23,
            'Peter': 19,
            'Andrew': 78,
            'Karren':45    }
"""
#Or we can do this:
ages = {}
#Add a couple of names to the dictionary
ages['Sue'] = 23
ages['Peter'] = 19
ages['Andrew'] = 78
ages['Karren'] = 45

#Use the function has_key() - 
#This function takes this form:
#function_name.has_key(key-name)
#It returns TRUE
#if the dictionary has key-name in it
#but returns FALSE if it doesn't.
#Remember - this is how 'if' statements work -
#they run if something is true
#and they don't when something is false.
if ages.has_key('Sue'):
    print "Sue is in the dictionary. She is", \
ages['Sue'], "years old"

else:
    print "Sue is not in the dictionary"

#Use the function keys() - 
#This function returns a list
#of all the names of the keys.
#E.g.
print "The following people are in the dictionary:"
print ages.keys()

#We can use the 'keys()' function to
#put all the key names in a list:
keys = ages.keys()

#We can use the 'values()' to get a list
#of all the values in a dictionary.
#You use the values() function:
print "People are aged the following:", \
ages.values()

#Put it in a list:
values = ages.values()

#We can use the 'sort()" to sort lists, with the sort() function
#It will sort all values in a list
#alphabetically, numerically, etc...
#You can't sort dictionaries - 
#they are in no particular order
print keys
keys.sort()
print keys

print values
values.sort()
print values

##We can use the  number of entries
#with the len() function:
print "The dictionary has", len(ages), "entries in it"