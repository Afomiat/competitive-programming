class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        all_win = set()
        one_lose = set()
        dic_lose = {}

        winners, losers = zip(*matches)

      
        all_win.update(set(winners) - set(losers))

       
        for loser in losers:
            dic_lose[loser] = dic_lose.get(loser, 0) + 1

        
        one_lose.update(key for key, value in dic_lose.items() if value == 1)

      
        all_win_list = sorted(list(all_win))
        one_lose_list = sorted(list(one_lose))

        return [all_win_list, one_lose_list]