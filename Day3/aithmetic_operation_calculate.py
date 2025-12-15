num1=int(input("enter 1st number:"))
num2=int(input("enter 2nd number:"))
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

def calculate():
    addition(num1,num2)
    subtraction(num1,num2)
    multiplication(num1,num2)
    divison(num1,num2)
    modulo(num1,num2)


def addition(num1,num2):
    print("The addition is:",num1+num2)

def subtraction(num1,num2):
    print("the subtraction is:",num1-num2)

def multiplication(num1,num2):
    print("The multiplicaton is:",num1*num2)

def divison(num1,num2):
    print("The division is:",num1/num2) 

def modulo(num1,num2):
    print("remainder is :",num1%num2)

calculate()