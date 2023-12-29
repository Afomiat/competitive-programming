class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        r = len(arr)
        result = []
        for i in range(len(arr)):
            max_idx = arr.index(r) + 1
            if 1 < max_idx < r:
                rev = arr[0:max_idx]
                rev.reverse()
                arr[0:max_idx] = rev
                end_rev = arr[:r]
                end_rev.reverse()
                arr[0:r] = end_rev
                result.append(max_idx)
                result.append(r)
                

            elif max_idx == 1:
                end_rev = arr[0:r]
                end_rev.reverse()
                arr[0:r] = end_rev
                result.append(r)
            r -= 1
        return result


