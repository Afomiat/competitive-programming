class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        
        window = blocks[:k]
        count_w = window.count('W')
        min_op = count_w

        for i in range(n - k + 1):
            
            if i > 0:
                if blocks[i - 1] == 'W':
                    count_w -= 1
                if blocks[k + i - 1] == 'W':
                    count_w += 1
            min_op = min(min_op, count_w)
           
        return min_op 
