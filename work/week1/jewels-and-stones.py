class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_dict = Counter(stones)
        count = 0
        for i in jewels:
            if i in stone_dict:
                count += stone_dict[i]
        return count