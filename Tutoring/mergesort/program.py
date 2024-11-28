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

# def merge_sort(arr):
#   # base case: return arr if it has less than one (already sorted)
#   # if not base case then divide array into two halves
#   # recursively sort each half
#   # merge the two sorted arrays
#   if len(arr) <= 1:
#     return arr
  
#   mid = len(arr) // 2
#   left = merge_sort(arr[:mid])
#   right = merge_sort(arr[mid:])

#   return merge(left, right)


# def merge(left, right):
# # Creates a new result array
# # Compares elements from both arrays
# # Adds the smaller element to the result
# # Continues until one array is exhausted
# # Adds any remaining elements
#   result = []
#   i = j = 0
#   while len(left) > i and len(right) > j:
#     if left[i] <= right[j]:
#       result.append(left[i])
#       i += 1
#     else:
#       result.append(right[j])
#       j += 1
  
#   result.extend(left[i:])
#   result.extend(right[j:])

#   return result
    

print("============================")
print("MergeSort Algorithm")
print("Current array: ")
print(rand_list)
print("")
print("Array after mergesort: ")
algo = merge_sort(rand_list, 0, len(rand_list) - 1)
print(algo)
print("============================")