import queue
# creates a stack
cards = queue.LifoQueue()

# adds elements to the top of the stack
cards.put(2)    
cards.put(3)  
cards.put(7)
cards.put(4)
cards.put(2)
cards.put(9)
cards.put(8)      

## prints number of elements of the stack
print('Number of stack elements:', cards.qsize())
if cards.qsize() >= 2:
    first = cards.get()
    second = cards.get()
    summ = first + second
    


# removes and prints elements from the top of the stack
summ1 = 0
while not cards.empty():
    summ1 += cards.get()

print('remaining summ: ', summ1)
    

print('Summary of 2 last numbers: ', summ)

"""
Note the order of the printed elements.
The last added element is printed first.
"""
