class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:

        def manhattan_distance(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

        your_distance = manhattan_distance([0, 0], target)

        for ghost_position in ghosts:
            ghost_distance = manhattan_distance(ghost_position, target)
            if ghost_distance <= your_distance:
                return False

        return True

            