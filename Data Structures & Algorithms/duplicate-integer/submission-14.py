class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newS = set()
        for n in nums:
            if newS and n in newS:
                return True
            newS.add(n)
        return False
