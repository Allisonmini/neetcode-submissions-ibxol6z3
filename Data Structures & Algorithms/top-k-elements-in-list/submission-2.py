class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map ={}
        for n in nums:
            map[n] = map.get(n, 0) +1

        freq = []
        for n in range(len(nums)+1):
            freq.append([])
        
        for i, n in map.items():
            freq[n].append(i)

        result = []
        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                result.append(j)
                if len(result) == k:
                    return result
                
