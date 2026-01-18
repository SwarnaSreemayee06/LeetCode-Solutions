class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        m=[]
        for x in nums:
            m.append(a*(x**2)+b*x+c)
        return list(sorted(m))
        
        