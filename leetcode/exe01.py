class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        i = 0
        
        while i < len(s):
            proximo = s[i+1] if i + 1 < len(s) else ''
            if s[i] == 'I':
                if proximo == 'V':
                    result += 4
                    i += 2
                    continue
            
                if proximo == 'X':
                    result += 9
                    i += 2
                    continue
                
                result += 1
                i += 1
                continue

            if s[i] == 'V':
                result += 5
                i += 1
                continue

            if s[i] == 'X':
                if proximo == 'L':
                    result += 40
                    i += 2
                    continue

                if proximo == 'C':
                    result += 90
                    i += 2
                    continue
                
                result += 10
                i += 1
                continue

            if s[i] == 'L':
                result += 50
                i += 1
                continue

            if s[i] == 'C':
                if proximo == 'D':
                    result += 400
                    i += 2
                    continue

                if proximo == 'M':
                    result += 900
                    i += 2
                    continue
                
                result += 100
                i += 1
                continue

            if s[i] == 'D':
                result += 500
                i += 1
                continue

            if s[i] == 'M':
                result += 1000
                i += 1
                continue
        
        return result
            
solucao = Solution()
print(solucao.romanToInt('DCXXI'))