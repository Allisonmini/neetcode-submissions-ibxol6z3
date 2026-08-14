class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map = {}
        l = 0
        res =0
        maxM = 0
        for r in range(len(s)):
            map[s[r]] = map.get(s[r],0) +1
            maxM = max(maxM, map[s[r]])
            while (r-l+1) -maxM > k:
                map[s[l]] -= 1
                l+=1
            res = max(res, r-l+1)

        return res
                            