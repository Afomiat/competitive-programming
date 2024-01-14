class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, n = 0, len(fruits)
        my_dict ={}
        maxi = 0

        for r in range(n):
            cur_val = fruits[r] 
            my_dict[cur_val] = my_dict.get(cur_val, 0) + 1

            if len(my_dict) > 2:
                my_dict[fruits[l]] -= 1
                if my_dict[fruits[l]] == 0:
                    del my_dict[fruits[l]]
                
                l += 1
            maxi = max(maxi, r - l + 1)  

        return maxi