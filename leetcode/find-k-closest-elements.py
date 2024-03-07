class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
      
        res = []
        ans = []
        for i in range(len(arr)) :
            res.append([abs(x - arr[i]), arr[i]])
        res.sort()

        for a, b in res:
            ans.append(b)
     
        ans = ans[:k]
        return sorted(ans)
    
        
      

