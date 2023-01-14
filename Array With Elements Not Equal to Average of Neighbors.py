class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n=len(nums)
        l=[-1]*n
        for i in range(0,n,2):
            l[i]=nums.pop(0)
        for i in range(n):
            if l[i]==-1:
                l[i]=nums.pop(0)
        return l
