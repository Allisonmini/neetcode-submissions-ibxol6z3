class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result =[1]* len(nums)

        pre = 1
        for i in range (len(nums)):
            result[i] = pre
            pre *= nums[i]
        sur = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= sur
            sur *= nums[i]

        return result






'''
    nums = [1, 2, 3, 4]
    pre = [1, 2, 6, 12] ---> pre =[1, 1, 2, 6]
    sur = [24, 24, 12, 4] ----> sur =[24, 12, 4, 1]
    result = [24, 12, 8, 6]
'''
        