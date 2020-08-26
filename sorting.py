import matplotlib.pyplot as plt
import matplotlib.animation as animation

# SORTING ALGORITHMS

# Helper function to swap element i and j in list A
def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

# Bubble Sort
# Idea: make multiple passes through the array, swapping out-of-order adjacent pairs
def bubblesort(A):
    swapped = True
    while (swapped):
        swapped = False
        for i in range(1, len(A)):
            if (A[i] < A[i-1]):
                swap(A, i, i-1)
                swapped = True
            yield A

# Insertion Sort
# Idea: iteratively increase the size of the array you are sorting
def insertionsort(A):
    for i in range(1, len(A)):
        val = A[i]
        for j in range(i, -1, -1):
            if (val >= A[j-1]):
                break
            A[j] = A[j-1]
            yield A
        A[j] = val

# Selection Sort
# Idea: swapping value in xth position with the xth smallest value
def selectionsort(A):
    for i in range(0, len(A)-1):
        min = i
        for j in range(i+1, len(A)):
            if (A[j] < A[min]):
                min = j
            yield A
        swap(A, i, min)
        yield A

# Quicksort
# Idea: choose an item to be a pivot, arrange so all items to the left of the
# pivot are smaller and all items to the right are larger. Recursively sort
# each of these partitions
def quicksort(A, lo, hi):
    if hi <= lo:
        return
    pivot = A[hi] # element to be placed in correct position
    index = lo - 1 # index of element that is smaller
    for i in range(lo, hi):
        if A[i] < pivot: # if current element is smaller than pivot
            index += 1
            swap(A, i, index)
        yield A
    swap(A, hi, index+1)
    yield A
    index += 1
    yield from quicksort(A, lo, index - 1) # before index
    yield from quicksort(A, index + 1, hi) # after index

# Mergesort
# Idea: recursively halve the list then merge back up
def mergesort(A, lo, hi):
    if hi <= lo:
        return
    mid = (lo + int((hi - lo + 1) / 2) - 1) # get midpoint
    yield from mergesort(A, lo, mid) # sort left
    yield from mergesort(A, mid + 1, hi) # sort right
    yield from merge(A, lo, mid, hi) # merge left and right

def merge(A, lo, mid, hi):
    res = [] # stores resulting sorted array
    leftPtr = lo # leftPtr iterates through left half
    rightPtr = mid + 1 # rightPtr iterates through right half
    while leftPtr <= mid and rightPtr <= hi:
        if A[leftPtr] < A[rightPtr]: # A[leftPtr] is smaller -> append this
            res.append(A[leftPtr])
            leftPtr += 1
        else: # A[rightPtr] is smaller -> append this
            res.append(A[rightPtr])
            rightPtr += 1
    res.extend(A[leftPtr:mid+1]) # add the rest of the array
    res.extend(A[rightPtr:hi+1])
    i = 0
    for val in res: # copy res into A
        A[lo + i] = val
        yield A
        i += 1

# Set up list to be sorted, get user input
inputs = input("Enter 'b' for bubblesort, 'i' for insertionsort, 's' for selectionsort, 'q' for quicksort, 'm' for mergesort\n")
A = [2,6,1,3,10,2,14,1,5,3,18,2,4,1,8,5,23,1,7,30] # list to be sorted
if inputs == "b":
    method = bubblesort(A)
elif inputs == "i":
    method = insertionsort(A)
elif inputs == "m":
    method = mergesort(A, 0, len(A) - 1)
elif inputs == "q":
    method = quicksort(A, 0, len(A) - 1)
else:
    method = selectionsort(A)

# Set up figure, axis, barplots
fig, ax = plt.subplots()
bar_rects = ax.bar(range(len(A)), A, align="edge")

# Do the animations
iteration = [0]
def update_fig(A, rects, iteration):
    for rect, val in zip(rects, A):
        rect.set_height(val)
    iteration[0] += 1
anim = animation.FuncAnimation(fig, func=update_fig, fargs=(bar_rects, iteration), frames=method, interval=1, repeat=False)

plt.show()
