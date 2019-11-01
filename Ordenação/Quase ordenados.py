from array import *
import time
import random

cont_selection = 0
cont_insertion = 0
cont_shell = 0

cont_quicksort = 0
cont_heap = 0
cont_merge = 0

def selection_sort(array):
    global cont_selection
    for index in range(0, len(array)):
        min_index = index
        for right in range(index + 1, len(array)):
            cont_selection += 1
            if array[right] < array[min_index]:
                min_index = right
        array[index], array[min_index] = array[min_index], array[index]
    return array

def insertion_sort(array):
    global cont_insertion
    for index in range(1, len(array)):
        current_element = array[index]
        cont_insertion += 1
        while index > 0 and array[index - 1] > current_element:

            array[index] = array[index - 1]
            index -= 1
        array[index] = current_element

    return array

def shell_sort(array):
    global cont_shell
    gap = len(array) // 2
    while gap > 0:
        for i in range(gap, len(array)):
            val = array[i]
            j=i
            cont_shell += 1
            while j >= gap and array[j - gap] > val:

                array[j] = array[j - gap]
                j -= gap
            array[j] = val
        gap //= 2
    return array

def partition(arr,low,high):
    global cont_quicksort
    i = (low - 1)
    pivot = arr[high]
    for j in range(low , high):
        cont_quicksort += 1
        if arr[j] < pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )

def quick_sort(array,low=0,high=None):
    global cont_quicksort
    if high == None:
        cont_quicksort += 1
        high = len(array)-1
    if low < high:
        cont_quicksort += 1
        pi = partition(array,low,high)
        quick_sort (array, low, pi-1)
        quick_sort (array, pi+1, high)
    return array

def heapify(arr, n, i):
    global cont_heap
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        cont_heap+=1
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
        if largest != i:
            arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr, n, largest)

def heap_sort(array):
    global cont_heap
    n = len(array)
    #constroi heapmax
    for i in range(n, -1, -1):
        cont_heap+=1
        heapify(array, n, i)
    #remove os elementos 1 a 1
    for i in range(n-1, 0, -1):
        cont_heap+=1
        array[i], array[0] = array[0], array[i]
    heapify(array, i, 0)
    return array

def merge_sort(array):
    global cont_merge
    if len(array) >1:
        cont_merge+=1
        mid = len(array)//2
        L = array[:mid]
        R = array[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            cont_merge+=1
            if L[i] < R[j]:
                array[k] = L[i]
                i+=1
            else:
                array[k] = R[j]
                j+=1
            k+=1
        while i < len(L):
            cont_merge+=1
            array[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            cont_merge+=1
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
    for i in range(5):
        vet1.append(i)
    for i in range(5):
        vet1.append(random.randrange(10))

inicio = time.time()
selection_sort(vet1)
print("O SELECTIONSORT REALIZOU ", cont_selection, " COMPARAÇÕES")
cont_selection = 0
fim = time.time() - inicio
print("TEMPO PARA O SELECTION SORT DO VETOR 1 É", fim)

inicio = time.time()
insertion_sort(vet1)
print("O INSERTIONSORT REALIZOU ", cont_insertion, " COMPARAÇÕES")
cont_insertion = 0
fim = time.time() - inicio
print("TEMPO PARA O INSERTION SORT DO VETOR 1 É", fim)

inicio = time.time()
shell_sort(vet1)
print("O SHELLSORT REALIZOU ", cont_shell, " COMPARAÇÕES")
cont_shell = 0
fim = time.time() - inicio
print("TEMPO PARA O SHELL SORT DO VETOR 1 É", fim)

inicio = time.time()
quick_sort(vet1, cont_quicksort)
print("O QUICKSORT REALIZOU ", cont_quicksort, " COMPARAÇÕES")
cont_quicksort = 0
fim = time.time() - inicio
print("TEMPO PARA O QUICK SORT DO VETOR 1 É", fim)

inicio = time.time()
heap_sort(vet1)
print("O HEAPSORT REALIZOU ", cont_heap, " COMPARAÇÕES")
cont_heap = 0
fim = time.time() - inicio
print("TEMPO PARA O HEAP SORT DO VETOR 1 É", fim)

inicio = time.time()
merge_sort(vet1)
print("O MERGESORT REALIZOU ", cont_merge, " COMPARAÇÕES")
cont_merge = 0
fim = time.time() - inicio
print("TEMPO PARA O MERGE SORT DO VETOR 1 É", fim)

for i in range (100):
    for i in range(5):
        vet2.append(i)
    for i in range(5):
        vet2.append(random.randrange(10))

inicio = time.time()
selection_sort(vet2)
print("O SELECTIONSORT REALIZOU ", cont_selection, " COMPARAÇÕES")
cont_selection = 0
fim = time.time() - inicio
print("TEMPO PARA O SELECTION SORT DO VETOR 2 É", fim)

inicio = time.time()
insertion_sort(vet2)
print("O INSERTIONSORT REALIZOU ", cont_insertion, " COMPARAÇÕES")
cont_insertion = 0
fim = time.time() - inicio
print("TEMPO PARA O INSERTION SORT DO VETOR 2 É", fim)

inicio = time.time()
shell_sort(vet2)
print("O SHELLSORT REALIZOU ", cont_shell, " COMPARAÇÕES")
cont_shell = 0
fim = time.time() - inicio
print("TEMPO PARA O SHELL SORT DO VETOR 2 É", fim)

inicio = time.time()
quick_sort(vet2, cont_quicksort)
print("O QUICKSORT REALIZOU ", cont_quicksort, " COMPARAÇÕES")
cont_quicksort = 0
fim = time.time() - inicio
print("TEMPO PARA O QUICK SORT DO VETOR 2 É", fim)

inicio = time.time()
heap_sort(vet2)
print("O HEAPSORT REALIZOU ", cont_heap, " COMPARAÇÕES")
cont_heap = 0
fim = time.time() - inicio
print("TEMPO PARA O HEAP SORT DO VETOR 2 É", fim)

inicio = time.time()
merge_sort(vet2)
print("O MERGESORT REALIZOU ", cont_merge, " COMPARAÇÕES")
cont_merge = 0
fim = time.time() - inicio
print("TEMPO PARA O MERGE SORT DO VETOR 2 É", fim)

for i in range (1000):
    for i in range(5):
        vet3.append(i)
    for i in range(5):
        vet3.append(random.randrange(10))

inicio = time.time()
selection_sort(vet3)
print("O SELECTIONSORT REALIZOU ", cont_selection, " COMPARAÇÕES")
cont_selection = 0
fim = time.time() - inicio
print("TEMPO PARA O SELECTION SORT DO VETOR 3 É", fim)

inicio = time.time()
insertion_sort(vet3)
print("O INSERTIONSORT REALIZOU ", cont_insertion, " COMPARAÇÕES")
cont_insertion = 0
fim = time.time() - inicio
print("TEMPO PARA O INSERTION SORT DO VETOR 3 É", fim)

inicio = time.time()
shell_sort(vet3)
print("O SHELLSORT REALIZOU ", cont_shell, " COMPARAÇÕES")
cont_shell = 0
fim = time.time() - inicio
print("TEMPO PARA O SHELL SORT DO VETOR 3 É", fim)

inicio = time.time()
quick_sort(vet3, cont_quicksort)
print("O QUICKSORT REALIZOU ", cont_quicksort, " COMPARAÇÕES")
cont_quicksort = 0
fim = time.time() - inicio
print("TEMPO PARA O QUICK SORT DO VETOR 3 É", fim)

inicio = time.time()
heap_sort(vet3)
print("O HEAPSORT REALIZOU ", cont_heap, " COMPARAÇÕES")
cont_heap = 0
fim = time.time() - inicio
print("TEMPO PARA O HEAP SORT DO VETOR 3 É", fim)

inicio = time.time()
merge_sort(vet3)
print("O MERGESORT REALIZOU ", cont_merge, " COMPARAÇÕES")
cont_merge = 0
fim = time.time() - inicio
print("TEMPO PARA O MERGE SORT DO VETOR 3 É", fim)

for i in range (10000):
    for i in range(5):
        vet4.append(i)
    for i in range(5):
        vet4.append(random.randrange(10))

inicio = time.time()
selection_sort(vet4)
print("O SELECTIONSORT REALIZOU ", cont_selection, " COMPARAÇÕES")
cont_selection = 0
fim = time.time() - inicio
print("TEMPO PARA O SELECTION SORT DO VETOR 4 É", fim)

inicio = time.time()
insertion_sort(vet4)
print("O INSERTIONSORT REALIZOU ", cont_insertion, " COMPARAÇÕES")
cont_insertion = 0
fim = time.time() - inicio
print("TEMPO PARA O INSERTION SORT DO VETOR 4 É", fim)

inicio = time.time()
shell_sort(vet4)
print("O SHELLSORT REALIZOU ", cont_shell, " COMPARAÇÕES")
cont_shell = 0
fim = time.time() - inicio
print("TEMPO PARA O SHELL SORT DO VETOR 4 É", fim)

inicio = time.time()
quick_sort(vet4, cont_quicksort)
print("O QUICKSORT REALIZOU ", cont_quicksort, " COMPARAÇÕES")
cont_quicksort = 0
fim = time.time() - inicio
print("TEMPO PARA O QUICK SORT DO VETOR 4 É", fim)

inicio = time.time()
heap_sort(vet4)
print("O HEAPSORT REALIZOU ", cont_heap, " COMPARAÇÕES")
cont_heap = 0
fim = time.time() - inicio
print("TEMPO PARA O HEAP SORT DO VETOR 4 É", fim)

inicio = time.time()
merge_sort(vet4)
print("O MERGESORT REALIZOU ", cont_merge, " COMPARAÇÕES")
cont_merge = 0
fim = time.time() - inicio
print("TEMPO PARA O MERGE SORT DO VETOR 4 É", fim)

for i in range (100000):
    for i in range(5):
        vet5.append(i)
    for i in range(5):
        vet5.append(random.randrange(10))

inicio = time.time()
selection_sort(vet5)
print("O SELECTIONSORT REALIZOU ", cont_selection, " COMPARAÇÕES")
cont_selection = 0
fim = time.time() - inicio
print("TEMPO PARA O SELECTION SORT DO VETOR 5 É", fim)

inicio = time.time()
insertion_sort(vet5)
print("O INSERTIONSORT REALIZOU ", cont_insertion, " COMPARAÇÕES")
cont_insertion = 0
fim = time.time() - inicio
print("TEMPO PARA O INSERTION SORT DO VETOR 5 É", fim)

inicio = time.time()
shell_sort(vet5)
print("O SHELLSORT REALIZOU ", cont_shell, " COMPARAÇÕES")
cont_shell = 0
fim = time.time() - inicio
print("TEMPO PARA O SHELL SORT DO VETOR 5 É", fim)

inicio = time.time()
quick_sort(vet5, cont_quicksort)
print("O QUICKSORT REALIZOU ", cont_quicksort, " COMPARAÇÕES")
cont_quicksort = 0
fim = time.time() - inicio
print("TEMPO PARA O QUICK SORT DO VETOR 5 É", fim)

inicio = time.time()
heap_sort(vet5)
print("O HEAPSORT REALIZOU ", cont_heap, " COMPARAÇÕES")
cont_heap = 0
fim = time.time() - inicio
print("TEMPO PARA O HEAP SORT DO VETOR 5 É", fim)

inicio = time.time()
merge_sort(vet5)
print("O MERGESORT REALIZOU ", cont_merge, " COMPARAÇÕES")
cont_merge = 0
fim = time.time() - inicio
print("TEMPO PARA O MERGE SORT DO VETOR 5 É", fim)

for i in range (1000000):
    for i in range(5):
        vet6.append(i)
    for i in range(5):
        vet6.append(random.randrange(10))

inicio = time.time()
selection_sort(vet6)
print("O SELECTIONSORT REALIZOU ", cont_selection, " COMPARAÇÕES")
cont_selection = 0
fim = time.time() - inicio
print("TEMPO PARA O SELECTION SORT DO VETOR 6 É", fim)

inicio = time.time()
insertion_sort(vet6)
print("O INSERTIONSORT REALIZOU ", cont_insertion, " COMPARAÇÕES")
cont_insertion = 0
fim = time.time() - inicio
print("TEMPO PARA O INSERTION SORT DO VETOR 6 É", fim)

inicio = time.time()
shell_sort(vet6)
print("O SHELLSORT REALIZOU ", cont_shell, " COMPARAÇÕES")
cont_shell = 0
fim = time.time() - inicio
print("TEMPO PARA O SHELL SORT DO VETOR 6 É", fim)

inicio = time.time()
quick_sort(vet6, cont_quicksort)
print("O QUICKSORT REALIZOU ", cont_quicksort, " COMPARAÇÕES")
cont_quicksort = 0
fim = time.time() - inicio
print("TEMPO PARA O QUICK SORT DO VETOR 6 É", fim)

inicio = time.time()
heap_sort(vet6)
print("O HEAPSORT REALIZOU ", cont_heap, " COMPARAÇÕES")
cont_heap = 0
fim = time.time() - inicio
print("TEMPO PARA O HEAP SORT DO VETOR 6 É", fim)

inicio = time.time()
merge_sort(vet6)
print("O MERGESORT REALIZOU ", cont_merge, " COMPARAÇÕES")
cont_merge = 0
fim = time.time() - inicio
print("TEMPO PARA O MERGE SORT DO VETOR 6 É", fim)