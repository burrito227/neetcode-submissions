class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def is_anagram(s1, s2) -> bool:
            """returns True if s1 and s2 are anagrams"""
            if len(s1) != len(s2):
                return False
            
            counter = {}

            for i in range(len(s1)):
                counter[s1[i]] = counter.get(s1[i], 0) + 1
                counter[s2[i]] = counter.get(s2[i], 0) - 1

            for count in counter.values():
                if count != 0:
                    return False
            
            return True

        anagrams = [[strs[0]]]

        for curr in strs[1:]:
            found_group = False
            for idx, group in enumerate(anagrams):
                # check the 1st string in each group for anagram
                if is_anagram(s1 = group[0], s2 = curr):
                    anagrams[idx].append(curr)
                    found_group = True
                    break

            # if curr not an anagram of a current group
            if not found_group:
                anagrams.append([curr])

        return anagrams