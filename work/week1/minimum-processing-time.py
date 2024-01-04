class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse = True)
        tasks.sort()
        j = 0
        min_time = 0

        for i in range(len(tasks)):
            min_time = max(min_time, processorTime[j] + tasks[i])
            if (i + 1) % 4 == 0:
                j += 1
        return min_time