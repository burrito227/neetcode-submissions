class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        max_count = 0

        for num in nums:
            if num - 1 in numbers:
                # then not the start of a sequence
                continue

            counter = 0
            curr = num
            while curr + 1 in numbers:
                counter += 1
                curr = curr + 1
            
            if counter >= max_count:
                max_count = counter + 1

        return max_count