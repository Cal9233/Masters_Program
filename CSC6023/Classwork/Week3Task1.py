# balanced 0-1 matrices

from itertools import combinations

def permutations(n):
    ones = list(combinations(list(range(n)),n//2))
    ans = []
    for o in ones:
        case = []
        for i in range(n):
            if (i in o):
                case.append(1)
            else:
                case.append(0)
        ans.append(case)
    return ans

def check(mat):
    n = len(mat[0])
    for j in range(n):
        acc0, acc1 = 0, 0
        for i in range(len(mat)):
            if (mat[i][j] == 1):
                acc1 += 1
            elif (mat[i][j] == 0):
                acc0 += 1
            if (acc0 > (n//2)) or (acc1 > n//2):
                return False
    return True

def layer(r, mat, perm, ans):
    for p in perm:
        mat.append(p)
        if check(mat):
            if (r+1 == len(p)):
                ans += 1
            else:
                ans = layer(r+1, mat, perm, ans)
        mat.pop()
    return ans

def balanced01mat():
    print("Computing the number of balanced matrices")
    n = [2, 4, 6, 8]
    for i in range(len(n)):
      perm = permutations(n[i])
      ans = layer(0, [], perm, 0)
      print(f"\n Balanced matrices for n = {n[i]} is {ans}")

# n = 2 is 2
# n = 4 is 90
# n = 6 is 297,200
# n = 8 is 450,283,905,890
balanced01mat()