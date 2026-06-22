class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for string in strs:
            s = "".join(sorted(string))

            if s in groups:
                groups[s].append(string)

            else:
                groups[s] = [string]

        curr = []
        for value in groups.values():
            curr.append(value)

        return curr
