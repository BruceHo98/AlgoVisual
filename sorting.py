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
    #return A

# Insertion Sort
# Idea: iteratively increase the size of the array you are sorting
def insertionsort(A):
    for i in range(1, len(A)):
        val = A[i]
        for j in range(i, 0, -1):
            if (val >= A[j-1]):
                break
            A[j] = A[j-1]
            yield A
        A[j] = val
    #return A

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
    #return A

# Quicksort TODO

# Mergesort TODO
def min(a, b):
    if (a < b):
        return a
    return b

def merge(A, lo, mid, hi):
    nitems = hi - lo + 1
    tmp = []
    i = lo
    j = mid+1
    k = 0
    while (i < mid+1 and j < hi+1):
        k = k + 1
        if (A[i] < A[j]):
            i = i + 1
            tmp[k] = A[i]
        else:
            j = j + 1
            tmp[k] = A[j]
    while (i < mid+1):
        k = k + 1
        i = i + 1
        tmp[k] = A[i]
    while (j < hi+1):
        k = k + 1
        j = j + 1
        tmp[k] = A[j]
    i = lo
    k = 0
    while (i < hi + 1):
        A[i] = tmp[k]
        i += 1
        k += 1

def mergesort(A, lo, hi):
    mid = int((lo + hi)/2)
    if (hi < lo+1):
        return
    mergesort(A, lo, mid)
    mergesort(A, mid+1, hi)
    merge(A, lo, mid, hi)

# Set up list to be sorted, get user input
inputs = input("Enter 'b' for bubblesort, 'i' for insertionsort, 's' for selectionsort\n")
A = [2,6,1,3,10,2,14,1,5,3,18,2,4,1,8,5,23,1,7,30] # list to be sorted
if inputs == "b":
    method = bubblesort(A)
elif inputs == "i":
    method = insertionsort(A)
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
