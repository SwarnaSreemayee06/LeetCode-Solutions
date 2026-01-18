class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=[x**2 for x in nums]
        return list(sorted((n)))
        