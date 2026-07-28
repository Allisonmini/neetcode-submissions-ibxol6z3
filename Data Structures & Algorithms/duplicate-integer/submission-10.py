class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapping = {}
        for n in nums:
            mapping[n] = mapping.get(n, 0) +1
            if mapping[n]> 1:
                return True
        return False