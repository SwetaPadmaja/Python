'''def max_3rdside(a,b):
    return a+b-1
print(max_3rdside(12,13))'''

'''def get_first_value(l):
  return l[0]
l=[12,23,45]
print(get_first_value(l))'''

'''Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis ... and space after each, and then the word is pronounced with a question mark ?.'''
'''def stutter(txt):
    newword= txt[0]+txt[1]+ "..."+txt[0]+txt[1]+"..."+txt
    return newword
txt="madam"
print(stutter(txt))'''

''' Create a function that takes two arguments: the original price and the discount percentage as integers and returns the final price after the discount.'''
'''def disc(org,disc):
    newprice= org-(org*disc/100)
    return newprice
print(disc(1000,10))'''
''' Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one decimal place.'''
'''import math
def rad_to_deg(r):
    d=math.degrees(r)
    d=round(d,1) # to round it to 1 decimal place
    return d
print(rad_to_deg(1))'''
''' Given the radius of a circle and the area of a square, return True if the circumference of the circle is greater than the square's perimeter and False if the square's perimeter is greater than the circumference of the circle.'''

'''import math
from math import pi
def circle_or_square(r,a):
    cf=2*pi*r
    s=math.sqrt(a)
    p=4*s
    if(cf>p):
        return True
    else :
        return False
print(circle_or_square(2,100))'''

''' In this challenge, establish if a given integer num is a Curzon number. If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number.

Given a non-negative integer num, implement a function that returns True if num is a Curzon number, or False otherwise.'''
'''def Curzon(a):
    pro1=1+2**a # i did  1 plus 2 elevated to number a 
    divisor=1+2*a # 1 plus 2 multplied with a
    if pro1%divisor==0: # checking whether its perfectly divide or not
        print("a is curzon number")
    else:
        print("a is not a curzon number")

Curzon(14)'''

'''Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.

Person	Relation
Darth Vader	--father
Leia	--sister
Han--	brother in law
R2D2-	droid'''

'''def relation_to_luke(name):
    d={"Darth Vader" : "father","Leia": "sister", "Han":"brother-in-law","R2D2":"droid"}
    return d[name]

print(relation_to_luke("Han"))'''

'''Create a function that takes an array of values resistance that are connected in series, and calculates the total resistance of the circuit in ohms. The ohm is the standard unit of electrical resistance in the International System of Units ( SI ).'''

'''def series_resistance(a,b,c):
    z=a+b+c 
    return z
val=str(series_resistance(12,10,12))
print( val+"ohms")'''

'''Create a function that takes two numbers and a mathematical operator + - / * and will perform a calculation with the given numbers.'''

'''def calculator(a,symbol,b):
    if symbol=="+":
        return a+b
    elif symbol== "*":
        return a*b
    elif symbol=="/":
        return a/b
print(calculator(3,"*",4))'''

'''factorial '''
'''def fact(x):
    fact1=1
    for i in range(1,x+1):
        fact1=fact1*i
    return fact1

print(fact(4))'''

''' print n natural numbers, n entered by user'''

'''def print_array(x):
    
    for i in range(1,x+1):
       print(i) 
    

print(print_array(5))'''




