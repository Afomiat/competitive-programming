class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives , tens = 0, 0

        for i in bills:
            if i == 5:
                fives += 1
            elif i == 10 and fives:
                tens += 1
                fives -= 1
            elif i == 20 and fives and tens:
                fives -= 1
                tens -= 1
            elif i == 20 and fives >= 3:
                fives -= 3
            else:
                return False
        return True