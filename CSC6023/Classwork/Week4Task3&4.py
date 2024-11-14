# knapsack unbounded - Greedy approach
def knapsack(v, w, cap):
    # array of values, array of weights
    rwv = []         # triplet ratio, weight, value, index
    for i in range(len(v)):
        rwv.append([v[i]/w[i], w[i], v[i], i])
    rwv.sort(reverse=True)    # sort from high to low rate
    ans = []                     # the list of added items
    tw = 0                                  # total weight
    found = True
    while (found):        # until no fitting item is found
        found = False
        for t in rwv:              # search an item to add
            if (t[1] + tw) <= cap:      # if the item fits
                ans.append(t[3])                  # add it
                tw += t[1]
                found = True
                break
    return ans           # returns the list of added items

def solve_knapsack(values, weights, capacity):
    print(f"\nCase: Distinct Items = {len(values)}, Values = {values}, Weights = {weights}, Capacity = {capacity}")
    answer = knapsack(values, weights, capacity)
    tv, tw = 0, 0
    for a in answer:
        tv += values[a]
        tw += weights[a]
    print(f"\nCase Result: Total Items = {len(answer)}, Total Value = {tv}, Total Weight = {tw}")

def helper_print(arr_output, values, weights, capacity):
    print("\n==================================================")
    print("\n               Original Output:")
    print("\n==================================================")
    print(f"\n{arr_output}")
    print("\n==================================================")
    print("\n               Formatted Output:")
    print("\n==================================================")
    solve_knapsack(values, weights, capacity)
    print("\n==================================================")

# Case 1
values1 = [5, 8, 12]
weights1 = [10, 20, 30]
capacity1 = 838

# Case 2
values2 = [3, 5, 7, 11, 13]
weights2 = [17, 23, 29, 31, 37]
capacity2 = 997

# Case 3
values3 = [5, 6, 7, 8]
weights3 = [25, 36, 49, 64]
capacity3 = 250

# Case 4
values4 = [5, 6, 7, 8]
weights4 = [25, 36, 49, 64]
capacity4 = 360

# Additional Test Case
values5 = [30, 14, 16, 9, 20]
weights5 = [6, 3, 4, 2, 6]
capacity5 = 40

print("\n___________________________")
print("\n === Task 3 Test Cases === ")
print("\n___________________________")
# Case 1: Total Items = 83, Total Value = 415, Total Weight = 830
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
helper_print(knapsack(values1, weights1, capacity1), values1, weights1, capacity1)
# Case 2: Total Items = 32, Total Value = 352, Total Weight = 992
# [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
helper_print(knapsack(values2, weights2, capacity2), values2, weights2, capacity2)
# Case 3: Total Items = 10, Total Value = 50, Total Weight = 250
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
helper_print(knapsack(values3, weights3, capacity3), values3, weights3, capacity3)
# Case 4: Total Items = 14, Total Value = 70, Total Weight = 350
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
helper_print(knapsack(values4, weights4, capacity4), values4, weights4, capacity4)

print("\n_____________________________________")
print("\n === Task 4 Additional Test Case === ")
print("\n_____________________________________")
# Additional Case: Total Items = 7, Total Value = 194, Total Weight = 39
# [0, 0, 0, 0, 0, 0, 1]
helper_print(knapsack(values5, weights5, capacity5), values5, weights5, capacity5)