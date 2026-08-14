class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = {}
        for i in range(len(nums)):
            mapp[nums[i]] = mapp.get(nums[i], 0) +1

        freq = []
        for i in range(len(nums)+1):
            freq.append([])

        for i, a in mapp.items():
            freq[a].append(i)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for each in freq[i]:
                res.append(each)
                if len(res) == k:
                    return res