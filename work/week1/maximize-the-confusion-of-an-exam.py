class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count_T, count_F = 0, 0
        l = 0
        max_length = 0
        
        for r in range(len(answerKey)):
            if answerKey[r] == 'T':
                count_T += 1
            else:
                count_F += 1
            
            while min(count_T, count_F) > k:
                if answerKey[l] == 'T':
                    count_T -= 1
                else:
                    count_F -= 1
                l += 1
            
            
            max_length = max(max_length, r - l + 1)
        
        return max_length