import random

rand_list = [random.randint(1, 100) for _ in range(10)]

# top to bottom approach

# ...

# bottom to top approach

def merge(arr, left, pivot, right):
  sub_left = arr[left:pivot + 1]
  sub_right = arr[pivot + 1: right + 1]
  # print(f"sub_left array: {sub_left}")
  # print(f"sub_right array: {sub_right}")
  i = j = 0
  k = left

  while i < len(sub_left) and j < len(sub_right):
    # print(f"sub_left[i] array: {sub_left[i]}")
    # print(f"sub_right[j] array: {sub_right[j]}")
    if sub_left[i] <= sub_right[j]:
      arr[k] = sub_left[i]
      i += 1
    else:
      arr[k] = sub_right[j]
      j += 1
    k += 1

  while i < len(sub_left):
    arr[k] = sub_left[i]
    i += 1
    k += 1

  while j < len(sub_right):
    arr[k] = sub_right[j]
    j += 1
    k += 1

def merge_sort(arr, left, right):
  if left < right:
    pivot = (left + right) // 2
    merge_sort(arr, left, pivot)
    merge_sort(arr, pivot + 1, right)
    merge(arr, left, pivot, right)
  return arr

print("============================")
print("MergeSort Algorithm")
ar = [4, 2, 9, 8, 1, 13, 3, 1]
print("Current array: ")
print(ar)
print("")
print("Array after mergesort: ")
algo = merge_sort(ar, 0, len(ar) - 1)
print(algo)
print("============================")

s = ['abc', 'bcd', 'cbaccd']
print(len(s))