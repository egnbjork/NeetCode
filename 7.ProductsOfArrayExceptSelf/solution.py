class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1] * length

        print(nums)
        #prefix
        prefix = 1
        for i in range(0, length):
            res[i] = res[i] * prefix
            prefix = prefix * nums[i]
        print(res)
        print(prefix)

        #postfix
        postfix = 1
        for i in range(length - 1, -1, -1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]

        return res
