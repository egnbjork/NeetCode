class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)

        for pr_i, pr_n in enumerate(prefix):
            if pr_i == 0:
                prefix[pr_i] = nums[pr_i]
            else:
                prefix[pr_i] = prefix[pr_i - 1] * nums[pr_i]

        for post_i in range(len(nums) - 1, -1, -1):
            if post_i == len(nums) - 1:
                postfix[post_i] = nums[post_i]
            else:
                postfix[post_i] = postfix[post_i + 1] * nums[post_i]

        for i, n in enumerate(nums):
            if i == 0:
                res.append(postfix[i + 1])
            elif i == len(nums) - 1:
                res.append(prefix[-2])
            else:
                num = prefix[i - 1] * postfix[i + 1]
                res.append(num)
                
        return res
