class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in diffs:
                return [diffs[diff], idx]

            if num not in diffs:
                diffs[num] = idx

        return [0, 0]