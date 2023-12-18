class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # boxes = list(map(int,boxes.split()))
        opp = 0
        result = []
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if boxes[i] == '0' and boxes[j] == '1':
                    opp += abs(i - j)
                elif boxes[i] == '1' and boxes[j] == '1':
                    opp += abs(i - j)
            result.append(opp)
            opp = 0
        return result

