def knapsack(v, w, cap):
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
    print("\nCase: Values =", values, "Weights =", weights, "Capacity =", capacity)
    answer = knapsack(values, weights, capacity)
    tv, tw = 0, 0
    for a in answer:
        print(f"Item - Value: {values[a]} - Weight: {weights[a]}")
        tv += values[a]
        tw += weights[a]
    print(f"Items: {len(answer)} - Total Value: {tv} - Total Weight: {tw}")

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
values5 = [10, 20, 30, 40, 50]
weights5 = [20, 30, 60, 90, 120]
capacity5 = 150

print("\n=== Running Original Test Cases ===")
solve_knapsack(values1, weights1, capacity1)
solve_knapsack(values2, weights2, capacity2)
solve_knapsack(values3, weights3, capacity3)
solve_knapsack(values4, weights4, capacity4)

print("\n=== Running Additional Test Case ===")
print("Expected result: Should select 2 items:")
print("- Item with value 20 and weight 30 (ratio: 0.67)")
print("- Item with value 10 and weight 20 (ratio: 0.50)")
print("Expected total: Value = 30, Weight = 50")
solve_knapsack(values5, weights5, capacity5)