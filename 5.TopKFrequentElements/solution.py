from sortedcontainers import SortedDict
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = SortedDict()
        for i in nums:
            count_nums[i] = count_nums.get(i, 0) + 1

        if len(count_nums) == 0:
            return []
        print(f"counted nums is {count_nums}")

        count_map = SortedDict()
        for p, v in count_nums.items():
            if v not in count_map:
                count_map[v] = []
            count_map[v].append(p)

        print(f"count map is {count_map}")
        print(list(reversed(count_map.values()))[:k])
        print(k)

        res = []
        for sublist in list(reversed(count_map.values()))[:k]:
            for num in sublist:
                res.append(num)
            if len(res) >= k:
                break
        return res
        
