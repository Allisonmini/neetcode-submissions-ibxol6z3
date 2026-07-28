class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        
        res = []
        for n in strs:
            count = [0]*26
            for each in n:
                count[ord(each)-ord('a')] += 1
            
            mapping[tuple(count)].append(n)
        
        for gp in mapping.values():
            res.append(gp)
        
        return res


        