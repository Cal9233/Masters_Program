import random

rand_list = [random.randint(1, 100) for _ in range(10)]

def merge(nums, left, pivot, right):
  sub_arr1 = nums[left:pivot + 1]
  sub_arr2 = nums[pivot + 1:right + 1]

  i = 0
  j = 0
  k = left

  while i < len(sub_arr1) and j < len(sub_arr2):
    if sub_arr1[i] <= sub_arr2[j]:
      nums[k] = sub_arr1[i]
      i += 1
    else:
      nums[k] = sub_arr2[j]
      j += 1
    k += 1

  while i < len(sub_arr1):
    nums[k] = sub_arr1[i]
    i += 1
    k += 1
  
  while j < len(sub_arr2):
    nums[k] = sub_arr2[j]
    j += 1
    k += 1



def merge_sort(nums, left, right):
  if left < right:
    pivot = (left + right) // 2
    merge_sort(nums, left, pivot)
    merge_sort(nums, pivot + 1, right)
    merge(nums, left, pivot, right)

  return nums

print("============================")
print("MergeSort Algorithm")
print("Current array: ")
print(rand_list)
print("")
print("Array after mergesort: ")
algo = merge_sort(rand_list, 0, len(rand_list) - 1)
print(algo)
print("============================")