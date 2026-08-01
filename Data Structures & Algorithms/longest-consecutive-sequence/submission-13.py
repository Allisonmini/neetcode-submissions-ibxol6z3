class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newSet = set(nums)
        res = 0

        for n in newSet:
            if n-1 not in newSet:
                length = 1
                while (n+length) in newSet:
                    length += 1
                

                res = max(res, length)
        return res
            


           
            