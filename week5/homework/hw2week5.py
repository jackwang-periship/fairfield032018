'''
Created on Apr 14, 2018

@author: student
'''
def fahrenheit(T):
    return ((float(9)/5)*T + 32)
#     result = ((float(9)/5)*T + 32)
#     return "%0.2f" % result

def celsius(T):
    return (float(5)/9)*(T-32)
#     result = (float(5)/9)*(T-32)
#     return "%0.2f" % result

tempC = (36.5, 37, 37.5, 39)
tempF = (91.3, 100, 110.5, 65.7)

F = map(fahrenheit, tempC)
C = map(celsius, tempF)

print F
print C

# Using lambda function
tempC = (10.5, 40, -5, 20)
tempF = (40.2, 10.8, 50.5, 80.7)

F = map(lambda x: ((float(9)/5)*x + 32), tempC)
C = map(lambda x: ((float(5)/9)*(x - 32)), tempF)
# F = map(lambda x: "{0:0.2f}".format((float(9)/5)*x + 32), tempC)
# C = map(lambda x: "{0:0.2f}".format((float(5)/9)*(x - 32)), tempF)
print "-"*30
print F
print C

result = filter(lambda x: x <= 90 and x >= 40, F)
print result

result = filter(lambda x: x <= 30 and x >= 15, C)
print result