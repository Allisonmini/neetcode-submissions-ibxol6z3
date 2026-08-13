class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pre = 1
        for i in range(len(nums)):
            res.append(pre)
            pre *= nums[i]
        
        sur = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= sur
            sur *= nums[i]

        return res


