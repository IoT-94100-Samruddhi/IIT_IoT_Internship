def overlapping(list1,list2):
    for i in list1:
        if i in list2:
            return True
    return False

a=[1,2,3,4,5]
b=[2,6,8,9,7]

print(overlapping(a,b))



    
