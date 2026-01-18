class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        p=0
        y=str(abs(x))
        if x>0:
            string=y[::-1]
            p=int(string) 
        if x<0:
            string='-'+y[::-1]
            p=int(string)
        if p>((2**31)-1) or p<(-2**31):
            p=0
        return p
        