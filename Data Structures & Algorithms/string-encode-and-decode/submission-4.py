class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}_{s}" for s in strs)


    def decode(self, s: str) -> List[str]:
        out = []

        length = 0
        start = 0
        end = 0

        while start < len(s):
            end = s.find('_', start)
            length = int(s[start:end])

            substring = s[end + 1:end + length + 1]
            out.append(substring)

            start = end + length + 1

        return out
