class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i1, n in enumerate(nums):
            prod = 1
            for i2, p in enumerate(nums):
                if i2 != i1:
                    print(f"multiplied {prod} * {p}")
                    prod = prod * p
            res.append(prod)
        return res
