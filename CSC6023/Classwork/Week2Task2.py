import random

list = [random.randint(1, 1000000) for _ in range(0, 1000)]

def mode_brute_force(arr):
    maxValue, maxCount = 0, 0
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        if count > maxCount:
            maxCount = count
            maxValue = arr[i]
    return maxValue

def mode(arr):
    arr.sort()
    current_count, current_value, max_count, max_value = 1, arr[0], 1, arr[0]
    for i in range(1, len(arr)):
        if arr[i] == current_value:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                max_value = current_value
            current_value = arr[i]
            current_count = 1
    if current_count > max_count:
        max_value = current_value
    return max_value
        
print(mode(list))