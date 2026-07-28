class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = defaultdict(int)

        for i, a in enumerate(nums):
            diff = target - a
            
            if diff in result:
                return [result[diff],i]
            result[a]= i
    