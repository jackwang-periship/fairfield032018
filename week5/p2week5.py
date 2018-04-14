'''
Created on Apr 14, 2018

@author: student
'''
"""
super added
MRO changed (explained below)
descriptors added
new style class objects cannot be raised unless derived from Exception (example below)
__slots__ added
MRO (Method Resolution Order) changed
It was mentioned in other answers, but here goes a concrete example of the difference between classic MRO and C3 MRO (used in new style classes).

The question is the order in which attributes (which include methods and member variables) are searched for in multiple inheritance.
"""

"""
Old Style
The f method of B returns "D.f()" (due to inheriting from D and not overriding). The f method of C returns "C.f()". 
Obviously since A inherits both B and C, there is some contention about which to use. Under the old rules (depth first left to right), 
it chooses the version in B, even though C is closer to A and in some sense "more authoritative". It's certainly a tricky question: 
it seems like it should have chosen the version in C, because after all, C has explicitly overridden the version in D and B hasn't. 
"""
class D:       # Note: Old-style
    def f(self): return "D.f()"
class B(D): pass
class C(D):
    def f(self): return "C.f()"
class A(B, C): pass

"""
New Style
Because C overrides D, it "wins". The actual logic here is to go up depth-first but stop when you find a class which is subclassed later on. 
For example, when looking for the definition of f to use, it tries to go up A - B - D, but stops when it realises that D is being subclassed by a class
which we haven't considered yet (C). So it considers C first before looking at D, and finds a "stronger" definition there.
"""
# class D(object):       # Note: New-style
#     def f(self): return "D.f()"
# class B(D): pass
# class C(D):
#     def f(self): return "C.f()"
# class A(B, C): pass
 
a = A()
print a.f()

