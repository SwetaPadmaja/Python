'''Create a function which returns the number of true values there are in an array.'''
'''def return_true(a):
    
    b=len(a)
    counter=0  
   
    for i in range(0,b):
        if a[i] == True:
           counter+=1
          # print(counter)
        
           
        
    return counter
a=[True,False,True,True,True]
print(return_true(a))'''

''' Write a function that takes a number and returns the perimeter of either a circle or a square. The input will be in the form (letter l, number num) where the letter will be either "s" for square, or "c" for circle, and the number will be the side of the square or the radius of the circle.
Dont use if-else 
Use the following formulas:

Perimeter of a square: 4 * side.
Perimeter of a circle: 6.28 * radius.'''

'''def perimeter(a,b): #a is letter c or s (circle or square) and  b is number
   match a:
    case "c": return 2*3.14*b
    case "s":return 4*b
    case default: return "not in list"


print(perimeter("s",7))'''


'''In a board game, a piece may advance 1-6 tiles forward depending on the number rolled on a six-sided dice. If you advance your piece onto the same tile as another player's piece, both of you earn a bonus.

Can you reach your friend's tile number in the next roll? Create a function that takes your position a and your friend's position b and returns a boolean representation of whether it's possible to earn a bonus on any dice roll.

Examples
possibleBonus(3, 7) ➞ true

possibleBonus(1, 9) ➞ false

possibleBonus(5, 3) ➞ false
Notes
You cannot move backward (which is why example #3 doesn't work).
If you are already on the same tile, return false, as you would be advancing away.
Expect only positive integer inputs.'''

'''def possible_bonus(a,b): # a is your position and b is your friend's position
    if a==b:
        print("You and your friend are in same position")
        return False
    elif a>b:
        print("You are ahead of your friend")
        return False
    elif a<b:
        if b-a>6:
            print("not possible in single turn")
        else:
            print("Possible, try to reach your friend")

possible_bonus(3,9)'''
'''Create a function that will return an integer number corresponding to the amount of digits in the given integer num.

Examples
num_of_digits(1000) ➞ 4

num_of_digits(12) ➞ 2

num_of_digits(1305981031) ➞ 10

num_of_digits(0) ➞ 1'''

'''def num_of_digits(n):
    newnum=n
    counter=0
    #print(counter)
    while int(n)>0:
        #print(counter)
        #print(int(n))
        counter+=1
        n=n/10
        
    print(f"the number of digits in {newnum} are {counter}")

num_of_digits(1000900)'''

''' Given three arguments ⁠— an object obj of the stolen items, the pets name and a value ⁠— return an object with that name and value in it (as key-value pairs).

Examples
addName({}, "Brutus", 300) ➞ { Brutus: 300 }

addName({ piano: 500 }, "Brutus", 400) ➞ { piano: 500, Brutus: 400 }

addName({ piano: 500, stereo: 300 }, "Caligula", 440) ➞ { piano: 500, stereo: 300, Caligula: 440 }'''

'''def addName(d,petname,number):
    d.update({petname:number})
    print(d)


d={} 
petname= "Brutus"
number=300
addName(d,petname,number)
petname2="piano"
number2=400   
addName(d,petname2,number2)
petname3="caligua"
number3=600
addName(d,petname3,number3)'''


#derivative of x^b= bx^b-1
'''Create a function that takes numbers b and m as arguments and returns the derivative of the function f(x)=x^b with respect to x evaluated at x=m, where b and m are constants.

Examples
derivative(1, 4) ➞ 1

derivative(3, -2) ➞ 12

derivative(4, -3) ➞ -108'''
'''
def derivative(m,b): #x=m
    answer=  m * b**(m-1)
    print(answer) 

derivative(3,-2)# answer should be 12 because it should be 3 X (-2)to the power of 3-1'''

''' to refer the figure of tetrahedron --> https://edabit.com/challenge/zRCyxKBBmr4F2x4Bv 
A tetrahedron is a pyramid with a triangular base and three sides. A tetrahedral number is a number of items within a tetrahedron.

Create a function that takes an integer n and returns the nth tetrahedral number.'''

'''Examples
tetra(2) ➞ 4

tetra(5) ➞ 35

tetra(6) ➞ 56
https://math.fandom.com/wiki/Tetrahedral_number  formula for tetrahedral number'''

'''def tetra(row):
    number= row*(row+1)*(row+2)/6
    print(int(number))

tetra(5)'''


'''
This Triangular Number Sequence is generated from a pattern of dots that form a triangle. The first 5 numbers of the sequence, or dots, are:

1, 3, 6, 10, 15
This means that the first triangle has just one dot, the second one has three dots, the third one has 6 dots and so on.

Write a function that returns the number of dots when given its corresponding triangle number of the sequence.
resource to find what is triangular number
https://www.mathsisfun.com/algebra/triangular-numbers.html
'''
'''def Triangular_number(number):
    dots= number*(number+1)/2
    print(int(dots))

Triangular_number(5)'''

'''Write a function that returns an anonymous function, which transforms its input by adding a particular suffix at the end.'''

'''def add_ly(word):
    newword= word+"ly"
    return newword

def add_less(word):
    newword1= word+"less"
    return newword1

print(add_ly("hopeful"))
print(add_less("fear"))'''






   

