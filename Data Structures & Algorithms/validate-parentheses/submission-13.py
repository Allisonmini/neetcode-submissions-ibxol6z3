class Solution:
    def isValid(self, s: str) -> bool:
        map = {")":"(", "}" : "{", "]": "["}

        res = []

        for c in s:
            if c in map:
                if res and res[-1] == map[c]:
                    res.pop()
                else:
                    return False
            else:
                res.append(c)
                
        if not res:
            return True
        else:
            return False
         