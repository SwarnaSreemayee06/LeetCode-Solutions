class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        y=0
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for x in d:
            if d[x]==1:
                y=x
        return y
        