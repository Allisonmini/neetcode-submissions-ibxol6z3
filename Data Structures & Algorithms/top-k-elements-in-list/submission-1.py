class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = []
        for i in range(len(nums)+1):
            bucket.append([])

        map = {}
        for n in nums:
            map[n] = map.get(n, 0) + 1

        
        for val, freq in map.items():
            bucket[freq].append(val)

        result = []
        for i in range(len(bucket)-1, 0, -1):
            for each in bucket[i]:
                result.append(each)
                if len(result) >= k:
                    return result
            