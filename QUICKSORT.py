import numpy as np
import time

print('''
                 
          ((((( ☻ )))))
             __|_|_     _____
            /\/\/\/\   |   ♥ \  Github : T1m0TP
          <|\/\/\/\/|_/ /____/  Instagram : @codeur.tim
           |___________/         
           |_|_|  /_/_/

''')

# We define a variable which will be our classic sort
toSort = np.random.randint(0, 2000, 1000)
print(toSort)

# We record the time
t1 = time.time()

# We create the quick sort function

def quick_sort(toSort):
    # If the variable is empty
    if len(toSort) == 0:
        return toSort
    # We define the first element which will be the pivot
    pivot = toSort[0]
    # We define all elements smaller than the pivot in a list called "minor"
    minor = []
    # We define all elements higher than the pivot in a list called "major"
    major = []

    for i in range(1, len(toSort)):
        # If the element is smaller than the pivot
        if toSort[i] < pivot:
            # We add it to the elements
            minor.append(toSort[i])
        # If it is equal
        if toSort[i] == pivot:
            # We add it either to smaller numbers or to higher numbers
            minor.append(toSort[i])
        # If it is higher
        if toSort[i] > pivot:
            major.append(toSort[i])

    return quick_sort(minor) + [pivot] + quick_sort(major)


print(quick_sort(toSort))

t2 = time.time()
t3 = t2-t1
print("The time is : ", t3)

t4 = time.time()

toSort = np.random.randint(0, 2000, 1000)
# We create 2 loops
for i in range(len(toSort)):
    for j in range(len(toSort)):
        # We create a condition which gives the order of arrangement of the numbers
        if toSort[i] <= toSort[j]:
            # We classify the numbers
            toSort[i], toSort[j] = toSort[j], toSort[i]
print(toSort)


t5 = time.time()
t6 = t5-t4
print("The time is : ", t6)

print("The delay is : ", t6-t3)
