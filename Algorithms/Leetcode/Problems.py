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
    
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Solution 1
        # Time Complexity: O(n) // loop through array once
        # Space Complexity: O(n) // Creating an array and storing with sums
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        return prefix
    
        # Solution 2
        # Time Complexity: O(n) // Looping through array one
        # Space Complexity: O(1) // Modifying original array using no extra space
        # for i in range(1, len(nums)):
        #     nums[i] += nums[i - 1]
        # return nums

    def minStartValue(self, nums):
        min_sum = curr_sum = 0
        
        # Find minimum sum
        for num in nums:
            curr_sum += num
            min_sum = min(min_sum, curr_sum)
        
        print(f"min_sum is: {min_sum}")
        print(f"after negating min_sum: {-min_sum}")
        print(f"after adding 1: {-min_sum + 1}")
        
        return max(1, -min_sum + 1)
    
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # For each index i, we need to find the average of elements from (i-k) to (i+k)
        # If we can't get k elements on either side, the result should be -1
        # We're using integer division for the average

        # How do we check if an index has k elements on both sides?
        # How do we efficiently calculate the sum of elements in the range?
        # How do we handle the division to get the average?
        # Would you like to try writing the conditions for checking if an index has k elements on both sides? 
        # What would be the valid range for i-k and i+k?
        n = len(nums)
        avgs = [-1] * n
        if 2 * k + 1 > k:
            return avgs
        window_sum = sum(nums[:2 * k + 1])
        for i in range(k, n - k):
            if i - k >= 0 and i + k < n:
                avgs = window_sum // (2 * k + 1)
            if i + k + 1 < n:
                window_sum += n[i + k + 1]
                window_sum -= n[i - k]
        return avgs
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
        left = ans = 0
        curr = 1
        for right in range(len(nums)):
            curr *= nums[right]
            while curr >= k:
                curr //= nums[left]
                left += 1
            ans += right - left + 1
        return ans

test = Solution()

# print(test.isValid(arr1))
# print(test.isValid(arr2))
# print(test.isValid(arr3))
# print(test.isValid(arr4))
# print(test.isValid(arr5))
# print(test.isValid(arr6))

# Test cases:
nums1 = [-3, 2, -3, 4, 2]     # min_sum = -4
nums2 = [1, 2, 3]             # min_sum = 0
nums3 = [1, -2]               # min_sum = -1
print(test.minStartValue(nums1))
print(test.minStartValue(nums2))
print(test.minStartValue(nums3))