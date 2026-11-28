class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            verdict = seen.get(target - n)
            if verdict is not None:
                return [verdict, i]
            seen[n] = i
        print(seen)
        return [-1, -1]