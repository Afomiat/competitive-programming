class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distance = []
        for point in points:
            x, y = point
            dist = sqrt(x**2 + y**2)
            distance.append(dist)

        point_dist = list(zip(points, distance))
        point_dist .sort(key=lambda x: x[1])

        result = []
        for i in range(k):
            result.append(point_dist[i][0])

        return result