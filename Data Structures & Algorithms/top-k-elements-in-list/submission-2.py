class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # init empty list to track frequency counters
        freq = [[] for _ in range(len(nums) + 1)]

        # init counter hash map
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        # the index of the list is equal to the how frequent the list of ints are
        for key, value in counter.items():
            freq[value].append(key)

        # reverse (start with most frequent ints)
        # build output list, return when len() of list equals k
        out = []
        for i in range(len(freq) - 1, 0, -1):
            # find all of the ints in the list at the given frequency i
            for number in freq[i]:
                out.append(number)

            if len(out) == k:
                return out