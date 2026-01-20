class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do 
        """
        y=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[y]=nums[i]
                y+=1
        while(y<len(nums)):
                nums[y]=0
                y+=1
