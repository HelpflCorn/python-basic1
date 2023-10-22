import time

def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

sample1 = list(range(10000))
sample2 = list(range(50000))
sample3 = list(range(100000))


start_time = time.time()
linear_search(sample1, 7000)
linear_time_sample1 = time.time() - start_time
print(linear_time_sample1)

start_time = time.time()
binary_search(sample1, 7000)
binary_time_sample1 = time.time() - start_time
print(binary_time_sample1)

start_time = time.time()
linear_search(sample2, 49000)
linear_time_sample2 = time.time() - start_time
print(linear_time_sample2)

start_time = time.time()
binary_search(sample2, 49000)
binary_time_sample2 = time.time() - start_time
print(binary_time_sample2)

start_time = time.time()
linear_search(sample3, 60000)
linear_time_sample3 = time.time() - start_time
print(linear_time_sample3)

start_time = time.time()
binary_search(sample3, 60000)
binary_time_sample3 = time.time() - start_time
print(binary_time_sample3)
