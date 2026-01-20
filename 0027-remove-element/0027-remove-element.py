class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[x],nums[i]=nums[i],nums[x]
                x+=1
        while val in nums:
            nums.remove(val)
        
        