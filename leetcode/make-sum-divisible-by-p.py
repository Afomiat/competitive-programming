class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target_remainder = sum(nums) % p
        if target_remainder == 0:
            return 0

        prefix_sum = 0
        prefix_sums = {0: -1}
        min_length = float('inf')
        current_remainder = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            current_remainder = prefix_sum % p
            complement_remainder = (current_remainder - target_remainder) % p

            if complement_remainder in prefix_sums:
                subarray_length = i - prefix_sums[complement_remainder]
                min_length = min(min_length, subarray_length)

            prefix_sums[current_remainder] = i

        return min_length if min_length < len(nums) else -1