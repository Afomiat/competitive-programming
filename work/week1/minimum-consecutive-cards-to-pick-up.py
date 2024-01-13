class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
     
        n = len(cards)
        l = 0
        my_dict = {}
        min_match = float('inf')

        for r in range(n):
            cur_val = cards[r]
            my_dict[cur_val] = my_dict.get(cur_val, 0) + 1

            while my_dict[cur_val] == 2:
                min_match = min(min_match, r - l + 1)
                my_dict[cards[l]] -= 1
                l += 1
        return min_match if min_match != float('inf') else -1
            
            