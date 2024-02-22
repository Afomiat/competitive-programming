class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()
        count = 0

        for i in range(len(tickets)):
            queue.append([tickets[i],i])
        
        while queue:
            val = queue.popleft()
            if val[0] > 0:
                val[0] -= 1
                count += 1
                if val[1] == k and val[0] == 0:
                    break
                queue.append(val)
            elif val[0] == 0 and val[1] != k:
                continue
            
        return count 

