class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        a = []
        count = 0
        result = ''
        rem = num
        if rem > 0:
            while rem > 0:
                val = rem // 10
                rem = rem % 10 
                a.append(rem)
                rem = val
                
            a.sort()
            i = 0
            while a[i] == 0:
                count += 1
                a = a[i + 1:]
                
            for i in a:
                result += str(i)
            result = result[0] + '0' * count + result[1:]
            
        
        else:
            num = str(num)
            
            for i in range(1, len(num)):
                a.append(int(num[i]))
            a.sort(reverse = True)
            print(a)
            result += num[0]
            
            for i in a:
                result += str(i)
            
        return int(result)