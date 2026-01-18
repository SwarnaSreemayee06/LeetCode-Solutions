class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Phase 1: Replace non-positive numbers and numbers > n with a placeholder (n+1)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        
        # Phase 2: Use array indices as hash keys - mark presence by making values negative
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])
        
        # Phase 3: Find the first positive number - its index + 1 is the answer
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        # If all positions are marked negative, the answer is n + 1
        return n + 1