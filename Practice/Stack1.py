#we can implement stack using LifoQueue function in python
from queue import LifoQueue
n=int(input("Enter number of elements:"))
stack=LifoQueue(maxsize=n) #stack of size n
print("Starting Insertion")
for i in range(3):
    stack.put(input("Enter Element:"))  #push operation
print("Staring Pop Operation")
for j in range(n):
    print("Popping: ",stack.get())  #pop operation
print("Check if stack is empty",stack.qsize())
#A similar mechanism can also be developed by using deque which is faster but that is for double ended queue
#While LifoQueue is specifically for implementing stacks.