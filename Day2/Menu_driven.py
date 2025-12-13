num1=int(input("enter 1st number:"))
num2=int(input("enter 2nd number:"))
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

def addition(num1,num2):
    print("The addition is:",num1+num2)

def subtraction(num1,num2):
    print("the subyraction is:",num1-num2)

def multiplication(num1,num2):
    print("The multiplicaton is:",num1*num2)

def divison(num1,num2):
    print("The division is:",num1/num2)

choice=int(input("enter user's choice"))

match choice:
    case 1:
         addition(num1,num2)

    case 2:
        subtraction(num1,num2)
    case 3:
        multiplication(num1,num2)
    case 4:
        divison(num1,num2)
    case default:
        print("invalid choice")
    
