class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for n in range(i, len(nums)):
                if i != n and (nums[i] + nums[n]) == target:
                    return [i, n]
        return []
