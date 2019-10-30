from array import *
import time
import random

def selection_sort(array):
    for index in range(0, len(array)):
        min_index = index
        for right in range(index + 1, len(array)):
            if array[right] < array[min_index]:
                min_index = right
        array[index], array[min_index] = array[min_index], array[index]
    return array

def insertion_sort(array):
    for index in range(1, len(array)):
        current_element = array[index]
        while index > 0 and array[index - 1] > current_element:
            array[index] = array[index - 1]
            index -= 1
        array[index] = current_element
    return array

def shell_sort(array): 
    gap = len(array) // 2 
    while gap > 0:
        for i in range(gap, len(array)):
            val = array[i]
            j=i
            while j >= gap and array[j - gap] > val:
                array[j] = array[j - gap]
                j -= gap 
            array[j] = val
        gap //= 2
    return array

def partition(arr,low,high): 
    i = (low - 1)
    pivot = arr[high]
    for j in range(low , high):
        if arr[j] < pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i] 
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 )

def quick_sort(array,low=0,high=None):
    if high == None:
        high = len(array)-1
    if low < high:
        pi = partition(array,low,high) 
        quick_sort (array, low, pi-1) 
        quick_sort (array, pi+1, high)
    return array

def heapify(arr, n, i): 
	largest = i 
	l = 2 * i + 1	 
	r = 2 * i + 2	 
	if l < n and arr[i] < arr[l]: 
		largest = l 
	if r < n and arr[largest] < arr[r]: 
		largest = r 
	if largest != i: 
		arr[i],arr[largest] = arr[largest],arr[i] 
		heapify(arr, n, largest) 

def heap_sort(array): 
    n = len(array) 
    #constroi heapmax
    for i in range(n, -1, -1): 
        heapify(array, n, i) 
    #remove os elementos 1 a 1
    for i in range(n-1, 0, -1): 
        array[i], array[0] = array[0], array[i]
    heapify(array, i, 0) 
    return array

def merge_sort(array): 
    if len(array) >1: 
        mid = len(array)//2 
        L = array[:mid] 
        R = array[mid:] 
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                array[k] = L[i] 
                i+=1
            else: 
                array[k] = R[j] 
                j+=1
            k+=1
        while i < len(L): 
            array[k] = L[i] 
            i+=1
            k+=1
        while j < len(R): 
            array[k] = R[j] 
            j+=1
            k+=1
    return array


vet1 = array('i', [])

vet2 = array('i', [])

vet3 = array('i', [])

vet4 = array('i', [])

vet5 = array('i', [])

vet6 = array('i', [])


for i in range (10):
    vet1.append(random.randrange(10))
    
selection_sort(vet1)
print("TEMPO PARA O SELECTION SORT DO VETOR 1 É", time.process_time())
insertion_sort(vet1)
print("TEMPO PARA O INSERTION SORT DO VETOR 1 É", time.process_time())
shell_sort(vet1)
print("TEMPO PARA O SHELL SORT DO VETOR 1 É", time.process_time())
quick_sort(vet1)
print("TEMPO PARA O QUICK SORT DO VETOR 1 É", time.process_time())
heap_sort(vet1)
print("TEMPO PARA O HEAP SORT DO VETOR 1 É", time.process_time())
merge_sort(vet1)
print("TEMPO PARA O MERGE SORT DO VETOR 1 É", time.process_time())

for i in range (100):
    vet2.append(random.randrange(100))
    
selection_sort(vet2)
print("TEMPO PARA O SELECTION SORT DO VETOR 2 É", time.process_time())
insertion_sort(vet2)
print("TEMPO PARA O INSERTION SORT DO VETOR 2 É", time.process_time())
shell_sort(vet2)
print("TEMPO PARA O SHELL SORT DO VETOR 2 É", time.process_time())
quick_sort(vet2)
print("TEMPO PARA O QUICK SORT DO VETOR 2 É", time.process_time())
heap_sort(vet2)
print("TEMPO PARA O HEAP SORT DO VETOR 2 É", time.process_time())
merge_sort(vet2)
print("TEMPO PARA O MERGE SORT DO VETOR 2 É", time.process_time())
    
for i in range (1000):
    vet3.append(random.randrange(1000))
    
selection_sort(vet3)
print("TEMPO PARA O SELECTION SORT DO VETOR 3 É", time.process_time())
insertion_sort(vet3)
print("TEMPO PARA O INSERTION SORT DO VETOR 3 É", time.process_time())
shell_sort(vet3)
print("TEMPO PARA O SHELL SORT DO VETOR 3 É", time.process_time())
quick_sort(vet3)
print("TEMPO PARA O QUICK SORT DO VETOR 3 É", time.process_time())
heap_sort(vet3)
print("TEMPO PARA O HEAP SORT DO VETOR 3 É", time.process_time())
merge_sort(vet3)
print("TEMPO PARA O MERGE SORT DO VETOR 3 É", time.process_time())
    
for i in range (10000):
    vet4.append(random.randrange(10000))
    
selection_sort(vet4)
print("TEMPO PARA O SELECTION SORT DO VETOR 4 É", time.process_time())
insertion_sort(vet4)
print("TEMPO PARA O INSERTION SORT DO VETOR 4 É", time.process_time())
shell_sort(vet4)
print("TEMPO PARA O SHELL SORT DO VETOR 4 É", time.process_time())
quick_sort(vet4)
print("TEMPO PARA O QUICK SORT DO VETOR 4 É", time.process_time())
heap_sort(vet4)
print("TEMPO PARA O HEAP SORT DO VETOR 4 É", time.process_time())
merge_sort(vet4)
print("TEMPO PARA O MERGE SORT DO VETOR 4 É", time.process_time())
    
for i in range (100000):
    vet5.append(random.randrange(100000))
    
selection_sort(vet5)
print("TEMPO PARA O SELECTION SORT DO VETOR 5 É", time.process_time())
insertion_sort(vet5)
print("TEMPO PARA O INSERTION SORT DO VETOR 5 É", time.process_time())
shell_sort(vet5)
print("TEMPO PARA O SHELL SORT DO VETOR 5 É", time.process_time())
quick_sort(vet5)
print("TEMPO PARA O QUICK SORT DO VETOR 5 É", time.process_time())
heap_sort(vet5)
print("TEMPO PARA O HEAP SORT DO VETOR 5 É", time.process_time())
merge_sort(vet5)
print("TEMPO PARA O MERGE SORT DO VETOR 5 É", time.process_time())
    
for i in range (1000000):
    vet6.append(random.randrange(1000000))
    
selection_sort(vet6)
print("TEMPO PARA O SELECTION SORT DO VETOR 6 É", time.process_time())
insertion_sort(vet6)
print("TEMPO PARA O INSERTION SORT DO VETOR 6 É", time.process_time())
shell_sort(vet6)
print("TEMPO PARA O SHELL SORT DO VETOR 6 É", time.process_time())
quick_sort(vet6)
print("TEMPO PARA O QUICK SORT DO VETOR 6 É", time.process_time())
heap_sort(vet6)
print("TEMPO PARA O HEAP SORT DO VETOR 6 É", time.process_time())
merge_sort(vet6)
print("TEMPO PARA O MERGE SORT DO VETOR 6 É", time.process_time())
