class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []

        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]

            
            if end1 >= start2 and end2 >= start1:
               
                result.append([max(start1, start2), min(end1, end2)])
            if end1 < end2:
                i += 1
            else:
                j += 1

        return result