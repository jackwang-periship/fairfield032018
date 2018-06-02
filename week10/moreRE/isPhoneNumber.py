'''
Created on Jun 1, 2018

@author: student
'''
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
        if text[3] != '-':
            return False
    for i in range(4, 7):
        if not text[i].isdecimal():
                return False
        if text[7] != '-':
            return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))

'''
On each iteration of the for loop, a new chunk of 12 characters from message 
is assigned to the variable chunk. For example, on the first iteration, i is 0, and chunk is assigned message[0:12] 
(that is, the string 'Call me at 4'). On the next iteration, i is 1, and chunk is assigned message[1:13] 
(the string 'all me at 41').
You pass chunk to isPhoneNumber() to see whether it matches the phone number pattern, and if so, you print the chunk.
Continue to loop through message, and eventually the 12 characters in chunk will be a phone number. 
The loop goes through the entire string, testing each 12-character piece and printing any chunk it finds 
that satisfies isPhoneNumber(). Once we’re done going through message, we print Done.
'''
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i + 12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

'''
The previous phone number–finding program works, but it uses a lot of code to do something limited: 
The isPhoneNumber() function is 17 lines but can find only one pattern of phone numbers. 
What about a phone number formatted like 415.555.4242 or (415) 555-4242? 
What if the phone number had an extension, like 415-555-4242 x99? The isPhoneNumber() function 
would fail to validate them. 
You could add yet more code for these additional patterns, but there is an easier way.
Regular expressions, called regexes for short, are descriptions for a pattern of text. 
For example, a \d in a regex stands for a digit character—that is, any single numeral 0 to 9. 
The regex \d\d\d-\d\d\d-\d\d\d\d is used by Python to match the same text the previous isPhoneNumber() function did: 
a string of three numbers, a hyphen, three more numbers, another hyphen, and four numbers. 
Any other string would not match the \d\d\d-\d\d\d-\d\d \d\d regex.
'''
import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

