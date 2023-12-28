class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        result = []
        min_len = min(len(nums1), len(nums2))
        n1_dict = Counter(nums1)
        n2_dict = Counter(nums2)

        if len(nums1) == min_len:
            for key, val in n1_dict.items():
                if key in n2_dict:
                    min_val = min(val, n2_dict[key])
                    for i in range(min_val):
                        result.append(key)
        else:
            for key, val in n2_dict.items():
                if key in n1_dict:
                    min_val = min(val, n1_dict[key])
                    for i in range(min_val):
                        result.append(key)
        return result