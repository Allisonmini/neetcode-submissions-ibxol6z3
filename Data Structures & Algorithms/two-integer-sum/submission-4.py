class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for each in range(len(nums)):
            com = target - nums[each] 
            if com in mapping:
                return [mapping[com], each]
            mapping[nums[each]] = each

