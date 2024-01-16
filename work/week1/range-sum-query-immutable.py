
class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = []
        cursum = 0
        for i in nums:
           cursum +=  i
           self.arr.append(cursum)

    def sumRange(self, left: int, right: int) -> int:
        
        rights = self.arr[right]
        lefts = self.arr[left-1] if left > 0 else 0
            
        return rights - lefts




# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)