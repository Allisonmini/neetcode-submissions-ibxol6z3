class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] *len(nums)
        pre = 1

        for i in range(len(nums)):
            result[i] = pre
            pre *= nums[i]
        
        sur = 1

        for j in range(len(nums)-1, -1, -1):
            result[j] *= sur
            sur *= nums[j]

        return result
            




'''
nums = [1,2,4,6]
pre = [1,1,2,8]
sur = [48,24,6,1]

res = [48, 24, 12, 8]

'''


