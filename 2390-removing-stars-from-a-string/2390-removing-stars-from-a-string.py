class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        p=''
        for i in s:
            if i!='*':
                stack.append(i)
            else:
                stack.pop()
        for i in stack:
            p+=i
        return p
    
        