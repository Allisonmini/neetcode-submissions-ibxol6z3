class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        res = 0

        while l<r:
            h = min(heights[r], heights[l])
            w = r - l
            a = h*w
            res = max(res, a)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res
                
