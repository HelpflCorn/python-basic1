import random
import time

array1 = [random.randint(1, 1000) for _ in range(1000)]
array2 = [random.randint(1, 1000) for _ in range(10000)]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

with open("sorting_results.txt", "w") as file:
    file.write("Array 1 (1000 elements):\n")
    
    start_time = time.time()
    bubble_sort(array1.copy())
    file.write(f"Bubble Sort: {time.time() - start_time} seconds\n")
    
    start_time = time.time()
    quick_sort(array1.copy())
    file.write(f"Quick Sort: {time.time() - start_time} seconds\n")
    
    start_time = time.time()
    insertion_sort(array1.copy())
    file.write(f"Insertion Sort: {time.time() - start_time} seconds\n")
    
    file.write("\nArray 2 (10000 elements):\n")
    
    start_time = time.time()
    bubble_sort(array2.copy())
    file.write(f"Bubble Sort: {time.time() - start_time} seconds\n")
    
    start_time = time.time()
    quick_sort(array2.copy())
    file.write(f"Quick Sort: {time.time() - start_time} seconds\n")
    
    start_time = time.time()
    insertion_sort(array2.copy())
    file.write(f"Insertion Sort: {time.time() - start_time} seconds\n")
