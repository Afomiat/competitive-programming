class Solution:
    def sortSentence(self, s: str) -> str:
        my_dict = {}
        result = []
        final = ''
        a = list(s.split())
        for i in a:
            key = i[-1]
            my_dict[key] = i[:-1]
            result.append(key)
        result.sort()

        for i in result:
            final += (my_dict[i] + ' ') 
           
        final = final.rstrip()
        return final
