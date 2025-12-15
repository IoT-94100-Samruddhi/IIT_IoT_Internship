#upper()-uppercase
msg="hello world"
print(msg.upper())

#lower()-lowercase
msg="SAMRUDDHEE"
print(msg.lower())

#title()-first letter capital
msg="hello world"
print(msg.title())

#strip():remove spaces from start and end 
msg=" hello world "
print(msg.strip())

#replace():replace part of string
msg=" hello world "
print(msg.replace("hello world","Samruddhee"))

#split():convert string to list
msg="DairyMilk,Ice-cream,Pastry"
print(msg.split(","))

#join():convert list to string
msg=["DairyMilk","Ice-cream","Pastry"]
print(",".join(msg))

#startswith():check begining 
msg="hello world"
print(msg.startswith("world"))

#endswith():check end
msg="hello world"
print(msg.endswith("world"))

#find():find index of substring
msg="I Love Singing"
print(msg.find("Love"))

#count():count occurance
msg="Samruddhee"
print(msg.count("e"))

#isalpha():only alphabets
msg="Samruddhee"
print(msg.isalpha())

#isdigit():only digits
msg="2060"
print(msg.isdigit())