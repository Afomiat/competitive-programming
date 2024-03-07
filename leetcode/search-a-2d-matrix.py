class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        l_2, r_2 = 0, len(matrix[0]) - 1
        # print(l, r)
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] == target or matrix[mid][-1] == target:
                return True
            elif target > matrix[mid][0] and target < matrix[mid][-1]:
                while l_2 <= r_2:
                    mid_2 = (l_2 + r_2) // 2
                    if matrix[mid][mid_2] > target:
                        r_2 = mid_2 - 1
                    elif matrix[mid][mid_2] < target:
                        l_2 = mid_2 + 1
                    else:
                        return True
                else:
                    return False
            elif matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][-1] < target:
                l = mid + 1
            
         
        return False