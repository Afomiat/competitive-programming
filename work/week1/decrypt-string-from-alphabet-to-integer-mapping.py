class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = []
        i = 0

        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
              
                mapped_char = chr(int(s[i:i + 2]) + ord('a') - 1)
                i += 3
            else:
                
                mapped_char = chr(int(s[i]) + ord('a') - 1)
                i += 1

            result.append(mapped_char)

        return ''.join(result)

