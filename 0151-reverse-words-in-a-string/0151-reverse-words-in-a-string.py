class Solution:
    def reverseWords(self, s: str) -> str:
        x=[]
        l=[]
        x=s.split()
        for i in range(1,len(x)):
            l.append(x[-i])
        l.append(x[0])
        return ' '.join(l)


        