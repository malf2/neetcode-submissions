class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        prev = {}
        for i, n in enumerate(nums):
            if n in prev and prev[n] != i:
                return True
            prev[n] = i
        return False

