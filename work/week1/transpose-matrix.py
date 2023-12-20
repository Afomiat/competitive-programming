class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = list(zip(*matrix))
        return transpose