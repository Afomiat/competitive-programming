class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rab_set = Counter(answers)
        count = 0
        print(rab_set)
      
        for key, val in rab_set.items():
           
            div = val // (key + 1)
            if val % (key + 1):
                count += ((div + 1) * (key + 1))
            else:
                count += (div * (key + 1))
        return count