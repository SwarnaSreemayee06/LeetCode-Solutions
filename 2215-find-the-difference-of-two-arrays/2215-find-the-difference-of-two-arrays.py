class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l=[]
        l1=set()
        l2=set()
        for i in nums1:
            if i not in nums2:
                l1.add(i)
        for j in nums2:
            if j not in nums1:
                l2.add(j)
        l.append(list(l1))
        l.append(list(l2))
        return l
        
        