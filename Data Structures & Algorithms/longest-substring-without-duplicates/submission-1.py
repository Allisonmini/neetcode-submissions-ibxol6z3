class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        newSet = set()
        result = 0
        l = 0

        for r in range(len(s)):
            while s[r] in newSet:
                newSet.remove(s[l])
                l += 1
            newSet.add(s[r])
            result = max(result, r-l + 1)
        return result


# '/ b c b c a'
# 'lr         ' >>>> set (a)
# 'l r        ' >>>> set (a,b)
# 'l   r      ' >>>> set (a,b,c)
# 'l     r    ' >>>> set (b, c)
# '  l   r    ' >>>> set (b, c)