class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        min_distance = float('-inf')
        sum1 = 0
        list_sum = sum(distance)
        clockwise = sum(distance[min(start,destination):max(start,destination)])
        
        counter_c = list_sum - clockwise
        min_distance = min(clockwise,counter_c )
        return min_distance
  