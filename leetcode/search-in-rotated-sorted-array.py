class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        maxx = max(nums)
        idx = indexOf(nums, maxx)
        print(idx)
        flag = False
        while l <= r:
            if target > maxx:
                return -1
            elif target == maxx:
                return idx
            elif nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            
            elif flag == False and target < maxx and target < nums[l]:
                l = idx + 1
                flag = True
            elif flag == False and target < maxx and target > nums[l]:
                r = idx - 1
                flag = True
            elif flag:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid

                if nums[mid] < target:
                    l = mid + 1
                if nums[mid] > target:
                    r = mid - 1
            
        return -1