class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x=[]
        z=0.0
        p=0
        x=sorted(nums1+nums2)
        if len(x)%2==1:
            y=int((len(x)/2))
            z=x[y]
        else:
            y=int((len(x)/2))
            p=int((len(x)/2)-1)
            z=(x[y]+x[p])/2
        return z
            
        