class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        frequencies = {}
        for i, v in enumerate(strs):
            freq = {}
            for s in v:
                freq[s] = 1 + freq.get(s, 0)
            frequencies[i] = [v, freq]

        groups = []
        prev = {}
        for k, v in frequencies.items():
            if k in prev:
                continue
            group = [v[0]]
            for k1, v1 in frequencies.items():
                if v[1] == v1[1] and k1 != k:
                    group.append(v1[0])
                    prev[k1] = v1
            groups.append(group)
            prev[k] = v
        return groups

        



