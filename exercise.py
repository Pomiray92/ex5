# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn


'''
from unittest import result


a = int(input(" Enter a Number 1: "))
b = int(input(" Enter a Number 2: "))
c = int(input(" Enter a Number 3: "))

result = a + b + c

if a == b == c:
    print(3*result)
else:
    print(result)
'''
'''
#Task2ex5
a = int(input(" Enter a Number 1: "))
b = int(input(" Enter a Number 2: "))

if a > b:    
    print("Dein ergebnis ist: ")

'''

'''

#Task3ex5

num = int(input(" Gebe ein Zahl ein: "))
if num % 2 == 0:
    print("Du hast die Zahl", num, "eingegeben, dein Zahl ist Geradezahl")
else:
    print("Du hast die Zahl", num, "eingegeben, dein Zahl ist Ungeradezahl")



#Task4ex5

from cmath import pi
import math

r = float(input("Input the radius of the circle:  "))
result = round((pi*r**2),2)
print("The area of the circle with radius", r, "is", result)


'''

#Task5ex5

'''

#guess = int(input("Guess a number between 1 and 10 until you get it rigth : "))
#if guess == 2:
    #print("Well done! You guessed rigth on the first try!")   
guess = 1      
while guess != 2: #bis guess nicht 2, ist hör nicht auf. 
    guess = int(input("Guess a number between 1 and 10 : "))

print("Well done! Now you got it")

'''

#Task6ex5


c = input("Input the scale schortcut you'd like to convert:(F - Fahrenheit, C - Celsius) ")
if c == "C" or c == "c":
    result1 = int(input("Input the value of temperature you'd like to convert: "))
    
elif c == "F" or c == "f":
    result2 = int(input("Input the value of temperature you'd like to convert: "))

