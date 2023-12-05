class Solution:
    def numberOfMatches(self, n: int) -> int:
        # if n is odd :n-1/2 == match
        # match = 0
        team = n
        sum_match = 0
        result = []
        while team > 1:
                if team % 2 != 0:
                    match = (team - 1)/2
                    result.append(match)
                    team = team - match
                else:
                    match = team/2
                    result.append(match)
                    team = team - match
        for num in result:
            sum_match += num
        return  int(sum_match)