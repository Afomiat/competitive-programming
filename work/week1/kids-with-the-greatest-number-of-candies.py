class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        # find max of the list
        max_list = max(candies)
        # new_candy = 0

        # add extara to each kids
        for candy in candies:
            
            new_candy = candy + extraCandies
            
            # if result > max of list: add tru to arr
            if new_candy >= max_list:
                result.append(True)
                new_candy = 0
            else:
                result.append(False)
                new_candy = 0
        return result
        