class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        
        # loop through the nums, record the integer count
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        def get_values(h):
            return counts[h]

        # sort based on integer count
        counts = sorted(counts, key=get_values, reverse=True)

        return counts[0:k]