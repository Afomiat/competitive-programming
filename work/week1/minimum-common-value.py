class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        set1 = set(nums1)
        set2 = set(nums2)
        inter_sect = list(set1 & set2)

        if not inter_sect:
            return -1
        else:
            inter_sect.sort()
          
            return inter_sect[0]

