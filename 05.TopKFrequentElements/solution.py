class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = {}
        for n in nums:
            count_nums[n] = (count_nums.get(n, 0) + 1)

        freq = [[] for _ in range(len(nums) + 1)]

        for num, count in count_nums.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if (len(res) >= k):
                    return res
        return res
