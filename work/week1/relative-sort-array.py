class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        arrx = []
        from collections import Counter
        my_dict = Counter(arr1)
        
        for i in arr2:
            for j in range(my_dict[i]):
                result.append(i)
        for i in arr1:
            if i not in arr2:
                arrx.append(i)
        arrx.sort()
        for i in arrx:
            result.append(i)
        
        return result
