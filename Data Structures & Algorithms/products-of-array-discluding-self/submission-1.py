class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [0] * n
        sur = [0] * n
        result = [0] * n

        pre[0] = 1
        sur[n-1] = 1
        for i in range (1, n):
            pre [i] = nums[i-1] * pre[i-1]

        for i in range(n-2, -1, -1):
            sur [i] = nums[i+1] * sur[i+1]

        for i in range(n):
            result[i] = pre[i] * sur[i]
        
        return result

        

            
