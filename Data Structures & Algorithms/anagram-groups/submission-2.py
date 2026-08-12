class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for i in range(len(strs)):
            table = [0] * 26
            for c in strs[i]:
                table[ord(c) - ord('a')] += 1

            map[tuple(table)].append(strs[i])
        return list(map.values())
        