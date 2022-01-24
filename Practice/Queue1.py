#we can implement stack using Queue function in python
from queue import Queue
n=int(input("Enter number of elements:"))  #total queue elements
q=Queue(maxsize=n)  #queue init
print("Insertion Begins")
for i in range(n):
    q.put(input("Enter Element: "))   #inserting into queue
print("Queue Full: ",q.full())   #checking if queue is full
print("Deletion Begins")
for j in range(n):
    print("Element Popped: ",q.get())   #deleting from queue
print("Queue Empty: ", q.empty())   #checking if queue is empty
#A similar mechanism can also be developed by using deque which is faster but that is for double ended queue
#While Queue is specifically for implementing queues.