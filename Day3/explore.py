#default parameter values of functions
def info(name="student"):
    print("Hello,", name)

# Function calls
info("Prem")
info()   # uses default value

#keyword arguments
def student_info(name, age, ID):
    print("Name:", name)
    print("Age:", age)
    print("Course ID:", ID)

# Calling function using keyword arguments
student_info(name="Prem",age=20,ID=69)

#passing one function to another
def add(a, b):
    return a + b

def operate(func, x, y):
    return func(x, y)

# Passing function add to another function
result = operate(add, 5, 3)
print("Result:", result)