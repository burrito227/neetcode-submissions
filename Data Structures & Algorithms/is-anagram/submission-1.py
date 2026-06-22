class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}

        if len(s) != len(t):
            return False
        
        for ch in s:
            if not ch in s_hash:
                s_hash[ch] = 1
            else:
                s_hash[ch] += 1

        for ch in t:
            if not ch in t_hash:
                t_hash[ch] = 1
            else:
                t_hash[ch] += 1

        for ch in s_hash.keys():
            if ch not in t_hash:
                return False
                
            if s_hash[ch] != t_hash[ch]:
                return False

        return True