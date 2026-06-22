class Solution:

    def encode(self, strs: List[str]) -> str:
        # <number of chars>_original_subscription
        encoded = ""

        for i, s in enumerate(strs):
            length = len(s)
            strs[i] = str(length) + "_" + s

        return "".join(strs)

    def decode(self, s: str) -> List[str]:
        out = []

        length = 0
        start = 0
        end = 0

        while start < len(s) - 1 and end < len(s) - 1:
            end = s.find('_', start)
            length = int(s[start:end])

            substring = s[end + 1:end + length + 1]
            out.append(substring)

            start = end + length + 1

        return out
