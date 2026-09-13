class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d=dict()
        p=set()
        l=[]
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1 
        for x in d.values():
            l.append(x)
            p.add(x)
        return len(p)==len(l)
        