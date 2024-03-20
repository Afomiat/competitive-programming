class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        arr = []
        ans = []
        my_dict = Counter(words)
       
        for key, val in my_dict.items():
            arr.append([val, key])
        arr.sort(reverse = True)
        # arr = arr[:k]
        maxx = arr[0][0]
        res = [[] for _ in range(maxx + 1)] 
        for i in arr:
            res[i[0]].append(i[1])
        for i in res:
            i.sort()
     
        for i in range(len(res)-1,-1, -1):
            if res[i]:
                ans.extend(res[i])
        print(ans)   
        return ans[:k]