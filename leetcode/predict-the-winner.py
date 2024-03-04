class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(p1, p2, turn):
            if p1 == p2:
                if turn:
                    return [nums[p1], 0]
                else:
                    return [0, nums[p2]]

            if turn:
                left = helper(p1 + 1, p2, not turn) 
                right = helper(p1, p2 - 1, not turn)
                left[0] += nums[p1]
                right[0] += nums[p2]
                if left[0] > right[0]:
                    return left
                else: return right

            else:
                left = helper(p1 + 1, p2, not turn) 
                right = helper(p1, p2 - 1, not turn)
                left[1] += nums[p1]
                right[1] += nums[p2]
                if left[1] > right[1]:
                    return left
                else: return right

        ans =  helper(0, len(nums) - 1, True)  
        # print(ans)
        return ans[0] >= ans[1]