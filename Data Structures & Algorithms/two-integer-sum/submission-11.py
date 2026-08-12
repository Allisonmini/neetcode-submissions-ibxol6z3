class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map ={}
        for i, a in enumerate(nums):
            diff = target - a
            if diff in map:
                return [map[diff], i]

            map[a] = i
        
            