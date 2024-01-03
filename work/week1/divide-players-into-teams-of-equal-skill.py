class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        result = []
        if len(skill) == 2:
            return skill[0] * skill[1]
        else:
            l, r = 0, len(skill) - 1
            my_sum = 0
            skill.sort()
            
            while l < r:
                result.append(skill[l] + skill[r])
                l += 1
                r -= 1
            l, r = 0, len(skill) - 1
            if all(x == result[0] for x in result):
                while l < r:
                    my_sum += skill[l] * skill[r]
                    l += 1
                    r -= 1
                return my_sum
            else:
                return -1
