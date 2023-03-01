from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide
from power import power
from modulo import modulo

# User input
print("Select operation.\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Power\n6.Modulo")

# Take input from the user
choice = input("Enter choice (1/2/3/4/5/6): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))

elif choice == '5':
   print(num1,"^",num2,"=", power(num1,num2))

elif choice == '6':
   print(num1,"%",num2,"=", modulo(num1,num2))

else:
   print("Invalid input")
