a=int(input("Enter number of elements in array:"))
lst=[]  #empty container
for c in range(a):   #for loop to enter elements
    element=int(input("Enter element:"))
    lst.append(element)
revlst=lst[::-1]   #taking from last element
print("Original Array\n",lst)
print("Reversed Array\n",revlst)
