class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if a == nums[i-1] and i > 0:
                continue
            
            l = i+1
            r = len(nums) - 1

            while l<r:
                tSum = a + nums[l] + nums[r]
                if tSum > 0:
                    r -= 1
                elif tSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res

        