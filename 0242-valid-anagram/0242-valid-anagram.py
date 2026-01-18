import collections 
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #return sorted(s)==sorted(t)
        one=collections.Counter(s)
        two=collections.Counter(t)
        return one==two
        