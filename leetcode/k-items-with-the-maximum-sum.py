class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        res = 0
        if k <= numOnes:
            res = k
        elif k > numOnes and k <= numOnes + numZeros:
            res = numOnes
        else:
            val = k - (numOnes + numZeros)
            res = numOnes - val
        return res