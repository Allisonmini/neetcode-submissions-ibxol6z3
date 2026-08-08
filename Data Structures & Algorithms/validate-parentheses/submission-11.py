class Solution:
    def isValid(self, s: str) -> bool:
        closing = {")":"(", "}":"{", "]": "["}
        res = []

        for c in s:
            if c in closing:
                if res and closing[c] == res[-1]:
                    res.pop()
                else: 
                    return False
            else:
                res.append(c)
        return not res

   

'''
'{()}]'
'''