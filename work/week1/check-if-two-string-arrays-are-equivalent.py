class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        conc1 = ''
        conc2 = ''
        for i in word1:
            conc1 += i
        
        for j in word2:
            conc2 += j
        return True if conc1 == conc2 else False

        