class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        result, first = 0, capacity
        for i, plant in enumerate(plants):
            if capacity >= plant:
                result += 1
            else:
                capacity = first
                result += 2 * i + 1
            capacity -= plant
        return result