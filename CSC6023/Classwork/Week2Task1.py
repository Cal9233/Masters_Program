import random

list = [random.randint(1, 1000000) for _ in range(0, 1000)]

def unique_brute_force(arr):
    ans = True
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] == arr[j]:
                ans = False
                break
            if not ans:
                break
    return ans 

def unique_transform_conquer(arr):
    arr.sort()
    for i in range(len(arr)):
        if arr[i-1] == arr[i]:
            return False
    return True


def main():
    print("Brute Force method for uniqueness in array:")
    print(unique_brute_force(list))

    print("Transformed-and-Conquered version for uniqueness in array:")
    print(unique_transform_conquer(list))

if __name__ == "__main__":
    main()