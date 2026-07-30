class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mapping = {}
        l = 0
        res = 0
        maxM = 0
        for r in range(len(s)):
            mapping[s[r]] = 1 + mapping.get(s[r], 0)
            maxM = max(maxM, mapping[s[r]])
            while (r - l + 1) - maxM > k:
                mapping[s[l]] -= 1
                l += 1
                
            
            res = max(res, r - l + 1)
        return res