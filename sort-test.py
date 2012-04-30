##
# Sorting Algorithm Examples in Python
#
# Matt Fisher - http://www.fisherinnovation.com
# Github - https://github.com/fisherinnovation/Sorting-Algorithms
#
# Based of code from vegaseat
##

import random   # For generating random numbers
import time     # For timing each sort function with time.clock()
DEBUG = False   # Set True to check results of each sort
N = 1000        # Number of elements in list
sortlist = []   # List of integer elements


# Setup basic randomized list.
for i in range(0, N):
    sortlist.append(random.randint(0, N-1))


# Prints the duration of a sort.
def print_timing(func):
    def wrapper(*arg):
        t1 = time.clock()
        res = func(*arg)
        t2 = time.clock()
        print '%s took %0.3fms' % (func.func_name, (t2-t1)*1000.0)
        return res
    return wrapper


# NOTE: Declare the @ decorator just above each sort function, invokes print_timing()


# Adaptive Merge Sort
@print_timing
def adaptive_merge_sort(list2):
    list2.sort() # Adaptive merge sort, built into Python since version 2.3
    

# Bubble Sort
@print_timing
def bubble_sort(list2):
    l = len(list2)
    
    for i in range(0, l - 1):
        swap_test = False
        
        for j in range(0, l - i - 1):
            if list2[j] > list2[j + 1]:
                list2[j], list2[j + 1] = list2[j + 1], list2[j]
            swap_test = True
        
        if swap_test == False:
            break
        
        
# Selection Sort
@print_timing
def selection_sort(list2):
    l = len(list2)
    
    for i in range(0, l):
        min = i
        for j in range(i + 1, l):
            if list2[j] < list2[min]:
                min = j
        list2[i], list2[min] = list2[min], list2[i]  
      
      
# Insertion Sort
@print_timing
def insertion_sort(list2):
    l = len(list2)
    for i in range(1, l):
        save = list2[i]
        j = i
        while j > 0 and list2[j - 1] > save:
            list2[j] = list2[j - 1]
            j -= 1
        list2[j] = save
  
  
# Quick Sort
@print_timing
def quick_sort(list2):
    l = len(list2)
    quick_sort_r(list2, 0, l - 1)
    
    
# Quick_sort_r, Recursive (used by quick_sort)
def quick_sort_r(list2, first, last):
    if last > first:
        pivot = partition(list2, first, last)
        #print 'Current Pivot: ' + str(pivot)
        
        quick_sort_r(list2, first, pivot - 1)
        quick_sort_r(list2, pivot + 1, last)
        
        
# Partition (Used by quick_sort_r)
def partition(list2, first, last):
    sred = (first + last)/2
    if list2[first] > list2 [sred]:
        list2[first], list2[sred] = list2[sred], list2[first]  
    if list2[first] > list2 [last]:
        list2[first], list2[last] = list2[last], list2[first]  
    if list2[sred] > list2[last]:
        list2[sred], list2[last] = list2[last], list2[sred]    
    list2 [sred], list2 [first] = list2[first], list2[sred]    
    pivot = first
    i = first + 1
    j = last
  
    while True:
        while i <= last and list2[i] <= list2[pivot]:
            i += 1
        while j >= first and list2[j] > list2[pivot]:
            j -= 1
        if i >= j:
            break
        else:
            list2[i], list2[j] = list2[j], list2[i]
    list2[j], list2[pivot] = list2[pivot], list2[j]
    return j


# Heap Sort
@print_timing
def heap_sort(list2):
    first = 0
    last = len(list2) - 1
    create_heap(list2, first, last)
    
    for i in range(last, first, -1):
        list2[i], list2[first] = list2[first], list2[i]
        establish_heap_property(list2, first, i - 1)
        
        
# Create Heap (Used by heap_sort)
def create_heap(list2, first, last):
    i = last/2
    while i >= first:
        establish_heap_property(list2, i, last)
        i -= 1
        
        
# Establish Heap Property (Used by create_heap)
def establish_heap_property(list2, first, last):
    while 2 * first + 1 <= last:
        k = 2 * first + 1
        if k < last and list2[k] < list2[k + 1]:
            k += 1
        if list2[first] >= list2[k]:
            break
        list2[first], list2[k] = list2[k], list2[first]
        first = k
        
        
# Merge Sort
@print_timing
def merge_sort(list2):
    merge_sort_r(list2, 0, len(list2) -1)
    
    
# Merge Sort Recursive (used by merge_sort)
def merge_sort_r(list2, first, last):
    if first < last:
        sred = (first + last)/2
        merge_sort_r(list2, first, sred)
        merge_sort_r(list2, sred + 1, last)
        merge(list2, first, last, sred)
        
        
# Merge (used by merge_sort_r)
def merge(list2, first, last, sred):
    helper_list = []
    i = first
    j = sred + 1
    
    while i <= sred and j <= last:
        if list2 [i] <= list2 [j]:
            helper_list.append(list2[i])
            i += 1
        else:
            helper_list.append(list2 [j])
            j += 1
    
    while i <= sred:
        helper_list.append(list2[i])
        i +=1
    
    while j <= last:
        helper_list.append(list2[j])
        j += 1
    
    for k in range(0, last - first + 1):
        list2[first + k] = helper_list [k]
        
        
# Test Sorted List by Printing the First 10 Elements
def printDebug(list2):
    for k in range(10):
        print list2[k],
    print
    
    
# Run Test if Script is Executed
if __name__ == "__main__" :
    print "Benchmarking 7 sorting algorithms \n" + str(N) + " randomized integers\nDebug Mode: " + str(DEBUG)
    print "----------------------------------------------------------------------------"
    
    # Make a true copy of sortlist each time
    list2 = list(sortlist)
    adaptive_merge_sort(list2)
    
    if DEBUG:
        printDebug(list2)
    
    list2 = list(sortlist)
    bubble_sort(list2)
    
    if DEBUG:
        printDebug(list2)
    
    list2 = list(sortlist)
    heap_sort(list2)
    
    if DEBUG:
        printDebug(list2)
    
    list2 = list(sortlist)
    insertion_sort(list2)
    
    if DEBUG:
        printDebug(list2)
    
    list2 = list(sortlist)
    merge_sort(list2)
    
    if DEBUG:
        printDebug(list2)
    
    list2 = list(sortlist)
    quick_sort(list2)
    
    if DEBUG:
        printDebug(list2)
   
    list2 = list(sortlist)
    selection_sort(list2)
    
    if DEBUG:
        printDebug(list2)
    
    # Final test
    list2 = list(sortlist)
    if DEBUG:
        print "Final Test: ",
        printDebug(list2)