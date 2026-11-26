class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setOfNums = set(nums)
        return len(setOfNums) != len(nums)