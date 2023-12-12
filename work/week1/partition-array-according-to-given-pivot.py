class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_piv = []
        great_piv = []
        equ_piv = []
        
        
        for num in range(len(nums)):
            if nums[num] < pivot:
                less_piv.append(nums[num])
            elif nums[num] > pivot:
                great_piv.append(nums[num])
            else:
                equ_piv.append(nums[num])
        result = less_piv + equ_piv + great_piv 
        return result