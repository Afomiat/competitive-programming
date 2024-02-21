class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda name: name[1])
        print(points)

        count = 0
        l, r = 0, 1
       
        idx = len(points) - 1
        while r < len(points):
            if points[l][1] < points[r][0]:
                count += 1
                l = r
                r += 1 
               
            else:
                r += 1
                
        return count + 1

    