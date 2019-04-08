from math import *
from tkinter import *

root = Tk()
labelA = Label(root, text="Enter First Number: ")


number1 = input("First Number: ")

operator = input("Operation: ")

number2 = input("Second Number: ")

result = 0

if operator == "+":
    result = float(number1) + float(number2)

elif operator == "*":
    result = float(number1) * float(number2)

elif operator == "-":
    result = float(number1) - float(number2)

elif operator == "/":
    result = float(number1) / float(number2)


print(result)

root.mainloop()



