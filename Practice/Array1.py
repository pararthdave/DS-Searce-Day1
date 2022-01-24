a=[1,2,3,4,5,'Hello']  #creating list (similar to array)
print(type(a)) #finding datatype
print(a)  #printing array
print(a[0]) #printing first elements
for x in a: #looping through elements
    print(x)
a.pop(0) #deleting first element
a.remove('Hello') #deleting elements with value
print(a, "Mission Successful") #verifying if element is deleted
print("End of Practice")
