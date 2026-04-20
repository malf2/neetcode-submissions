class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for v in s:
            if v in s_map:
                s_map[v] += 1
            else:
                s_map[v] = 1
        
        for v in t:
            if v in t_map:
                t_map[v] += 1
            else:
                t_map[v] = 1
        
        if s_map == t_map:
            return True
        return False
            
