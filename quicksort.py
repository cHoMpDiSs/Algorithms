from random import randint

#random array for testing
def create_array(size = 10, max = 50):
    return [randint(0,max) for _ in range(size)]

# applies quicksort to input array in place

def partition(a, low, high): # partition divides the array into two parts

    i = low # setting our pointers
    j = high -1
    pivot = a[high]
    while i < j: # i and j never cross
        while i < high and a[i] < pivot: #searching for values to swap
            i += 1
        while j > low and a[j] >= pivot:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i] # swapping values
        
    if a[i] > pivot:
        a[i], a[high] = a[high],a[i] # changing pivot
    return i


def quicksort(a, low=0, high=None):
    if high == None:
        high = len(a)-1
    if low < high:
        p_idx = partition(a, low, high) # partition around pivot
        quicksort(a,low, p_idx -1) # sort lower half
        quicksort(a, p_idx+1,high) # sort upper half

a = create_array()
print ("unsorted array:" , a)
quicksort(a)
print("sorted array", a)
