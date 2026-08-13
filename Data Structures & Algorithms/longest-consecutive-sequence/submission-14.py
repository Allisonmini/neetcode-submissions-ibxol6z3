class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newS = set(nums)

        longest = 0
        for n in newS:
            if (n-1) not in newS:
                length = 1
                while n + length in newS:
                    length += 1
                    
                longest = max(longest, length)
        return longest
            
            