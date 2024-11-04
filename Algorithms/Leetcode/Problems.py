class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # nums array is already in ascending order, so start loop from the end
        # creating an array with existing zeros that match length of nums array and updating them via index is more sufficient than appending, because we already created the set space, we're not creating more space for every loop
        n = len(nums)
        left = 0
        right = n - 1
        result = [0] * n
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] * nums[left]
                left += 1
            else:
                result[i] = nums[right] * nums[right]
                right -= 1
        return result
  
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # we want to ignore open brackets
        check = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for i in range(len(s)):
            if s[i] in check:
                if len(stack) > 0 and check[s[i]] != stack[-1]:
                    return False
                else:
                    if len(stack) > 0:
                        stack.pop()
                    else:
                        return False
            else:
                stack.append(s[i])
        return len(stack) == 0

    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        for i in range(k, len(nums)):
            curr = curr + nums[i] - nums[i - k]
            max_sum = max(max_sum, curr_sum)
        return max_sum / k

    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = zero_count = max_length = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length


arr1 = "()"
arr2 = "()[]{}"
arr3 = "(]"
arr4 = "([])"
arr5 = "([{}])"
arr6 = "]})([{}])"

test = Solution()

# print(test.isValid(arr1))
# print(test.isValid(arr2))
# print(test.isValid(arr3))
# print(test.isValid(arr4))
# print(test.isValid(arr5))
# print(test.isValid(arr6))

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(test.longestOnes(nums, k))