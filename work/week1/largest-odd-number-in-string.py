# class Solution:
#     def largestOddNumber(self, num: str) -> str:
#         num = int(num)
        
#         if num % 2 != 0:
#             return str(num)
#         else:
#             num_str = str(num)
#             num_list = list(map(int, num_str))
            
#             if all(n % 2 == 0 for n in num_list):
#                 return ""

#             while num % 2 == 0:
#                 if num_list and num_list[-1] % 2 == 0:
#                     num_list.pop()
#                     num_str = ''.join(map(str, num_list))
#                     num = int(num_str)
#                 else:
#                     break

#             return str(num)

class Solution:
    def largestOddNumber(self, num: str) -> str:
        num_str = str(num)

        if int(num_str[-1]) % 2 != 0:
            return num_str
        else:
            num_list = list(map(int, num_str))

            if all(n % 2 == 0 for n in num_list):
                return ""

            while int(num_list[-1]) % 2 == 0:
                num_list.pop()

            return ''.join(map(str, num_list))