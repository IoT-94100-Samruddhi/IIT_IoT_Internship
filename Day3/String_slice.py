text=input("enter name:")
#Full string
print("full string:",text[:])

#Fisrt 5 characters 
print("First five characters:",text[0:5])

#last three letters
print("First five characters:",text[-3:])

#character from index 2 to 6
print("character from index 2 to 6:",text[2:7])

#reverse string
print("reverse string:",text[::-1])

#every 2nd char
print("every 2nd char:",text[::2])

#slice from index 3 to end
print("slice from index 3 to end:",text[3:])

#slice from start to index 4
print("slice from start to index 4:",text[:5])

#negative indexing demo
print("negative indexing:",text[-5:-1])

#reverse every alternate char
print("reverse every alternate char:",text[::-2])