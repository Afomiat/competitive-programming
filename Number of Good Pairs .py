class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d={}
        count=0
        for i in nums:
            if i in d:
                if d[i]==1:
                    count+=1
                else:
                    count+=d[i]
                d[i]+=1 # if i is in  nums d[i] will always increase
            else:
                d[i]=1
        return count
