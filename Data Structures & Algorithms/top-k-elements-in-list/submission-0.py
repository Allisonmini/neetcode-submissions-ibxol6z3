class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = {}
        for n in nums:
            mapping[n] = mapping.get(n, 0) +1

        freq = []
        for i in range(len(nums)+1):
            freq.append([])

        for val,f in mapping.items():
            freq[f].append(val)

        result = []
        for i in range (len(freq)-1, 0, -1):
            for each in freq[i]:
                result.append(each)
                if len(result)== k:
                    return result

        