import random

CONST = 32

def min_run(n):
    r = 0
    while n >= CONST:
        r |= n & 1
        n >>= 1
    return n + r

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        item = arr[i]
        j = i - 1
        while j >= left and arr[j] > item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = item

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def timsort(arr):
    n = len(arr)
    min_r = min_run(n)
    for start in range(0, n, min_r):
        end = min(start + min_r - 1, n - 1)
        insertion_sort(arr, start, end)
    size = min_r
    while size < n:
        for left in range(0, n, size * 2):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            if mid < right:
                merged_arr = merge(arr[left:mid + 1], arr[mid + 1:right + 1])
                arr[left:left + len(merged_arr)] = merged_arr
        size *= 2

#Test
arr = [random.randint(-1000, 1000) for _ in range(random.randint(10, 100))]
timsort(arr)
print("Array length:", len(arr))
print("Sorted:", arr)