class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newSet = set(nums)

        result = 0
# (2, 20, 4, 10, 3, 5)
        for n in newSet:
            if (n-1) not in newSet:
                length = 1

                while (n+length) in newSet:
                    length += 1
                
                result = max(length, result) 
        return result

''' Time = O(n) Space = O(n) '''