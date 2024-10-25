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
    value, count = 0, 0
    for i in range(len(arr)):
        value = arr[i]
        if arr[i + 1] == value:
            count += 1
