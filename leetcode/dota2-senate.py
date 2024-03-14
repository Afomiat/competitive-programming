class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R = deque()
        D = deque()
        for i in range(len(senate)):
            if senate[i] == 'R':
                R.append(i)
            else:
                D.append(i)
        while R and D:
            if R[0] < D[0]:
                D.popleft()
                R.append(R.popleft() + len(senate))
            elif D[0] < R[0]:
                R.popleft()
                D.append(D.popleft() + len(senate))

        return 'Radiant' if R else 'Dire' 
