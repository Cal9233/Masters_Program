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
        # n = len(nums)
        # avgs = [-1] * n
        # window_len = 2 * k + 1
        # start = k
        # end = n - k

        # if end < start:
        #     return avgs
        
        # for i in range(start, end):
        #     for j in range(i - k, i + k):
        #         avgs[i] += nums[j]
        #     avgs[i] = (avgs[i] + 1) // window_len
        
        # return avgs
    
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
    
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 
    
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def helper(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            return left.val == right.val and helper(left.left, right.right) and helper(left.right, right.left)
        if root is None:
            return True
        return helper(root.left, root.right)
    
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        dic = set()
        for i in range(len(sentence)):
            dic.add(sentence[i])
        return len(dic) == 26
    
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 1
        # nums.sort()
        # count = 0
        # for i in range(len(nums)):
        #     if nums[i] != count:
        #         return count
        #     count += 1
        # return count
        
        # Solution 2
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2 
        actual_sum = sum(nums)
        return expected_sum - actual_sum

    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        num_set = set(arr)
        count = 0
        for i in arr:
            if i + 1 in num_set:
                count += 1
        return count
    
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s.replace(" ", "")
        current_num = 0
        stack = []
        operation = '+'
        for i, char in enumerate(s):
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            if char in '+-*/' or i == len(s) - 1:
                if operation == '+':
                    stack.append(current_num)
                elif operation == '-':
                    stack.append(-current_num)
                elif operation == '*':
                    stack.append(stack.pop() * current_num)
                elif operation == '/':
                    prev = stack.pop()
                    if prev < 0 and current_num > 0:
                        stack.append(-())
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        if root is None:
            return result
        queue = [[root, 0]]

        while queue:
            node, level = queue.pop(0)
            if len(result) == level:
                result.append(node.val)
            if node.right is not None:
                queue.append([node.right, level + 1])
            elif node.left is not None:
                queue.append([node.left, level + 1])
        return result
    
    def deepestLeavesSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        def max_depth(root):
            if root is None:
                return 0
            
            left = max_depth(root.left)
            right = max_depth(root.right)
            
            if left is None:
                return right + 1
            if right is None:
                return left + 1
            
            return max(left, right) + 1
        
        # create a function that sums the depth that takes root, current depth and target depth as params
        # if current depth is equal to the target depth you want to return the value
        # use recursion to go to next level if it does not meet that condition
        
        def sum_of_depth(root, curr_dep, target_dep):
            if root is None:
                return 0
            
            if curr_dep == target_dep:
                return root.val
            
            left = sum_of_depth(root.left, curr_dep + 1, target_dep)
            right = sum_of_depth(root.right, curr_dep + 1, target_dep)
            
            return left + right
        
        level = max_depth(root)
        return sum_of_depth(root, 1, level)
    
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        # initialize variables that represent result, current tree level, list of values in tree level
        # and queue
        # use BFS to traverse through tree, so use queue
        # in queue you want to see if the levels are even or odd to reverse them
        # update current level after ever traverse, and reset the list of values in tree level after   
        # the traverse
        # Don't forget to add the final values in deepest level to result
    
        if root is None:
            return []
        
        result = []
        curr_lvl = 0
        curr_vals = []
        queue = [(root, 0)]
        
        while queue:
            node, level = queue.pop(0)
            
            if level > curr_lvl:
                if curr_lvl % 2:
                    curr_vals.reverse()
                result.append(curr_vals)
                curr_lvl = level
                curr_vals = []
            curr_vals.append(node.val)
            if node.left:
                queue.append([node.left, curr_lvl + 1])
            if node.right:
                queue.append([node.right, curr_lvl + 1])
        
        if curr_vals:
            if curr_lvl % 2:
                curr_vals.reverse()
            result.append(curr_vals)
        return result
    
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        # nums[:] modifies and slices ORIGINAL list
        nums[:] = nums[n-k:] + nums[:n-k]

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= len(nums) - 1:
                return True

        return True


test = Solution()

# print(test.isValid(arr1))
# print(test.isValid(arr2))
# print(test.isValid(arr3))
# print(test.isValid(arr4))
# print(test.isValid(arr5))
# print(test.isValid(arr6))

# Test cases:
nums = [2,3,1,1,4]
# print(test.minStartValue(nums2))
# print(test.minStartValue(nums3))
print(test.canJump(nums))