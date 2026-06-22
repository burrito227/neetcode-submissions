class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashtable = {}
        for num in nums:
            if num in hashtable:
                return True
            else:
                hashtable[num] = True

        return False

        