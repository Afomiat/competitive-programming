class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) < 3:
            return False
        else:
            if arr == sorted(arr) or arr == sorted(arr, reverse = True):
                return False
            else:
                for i in range(len(arr) + 1):
                    if arr[i] < arr[i + 1]:
                        pass
                    else:
                        break
             
                return all(arr[j] > arr[j + 1] for j in range(i, len(arr) - 1))