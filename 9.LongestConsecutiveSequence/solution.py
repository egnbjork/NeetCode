class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0

        longest_seq = 1
        seq = 0
        sorted_nums = sorted(nums)
        last_num = sys.float_info.max

        print(sorted_nums)
        for num in sorted_nums:
            if num - 1 == last_num:
                seq = seq + 1
                last_num = num
            elif(num == last_num):
                continue
            else:
                seq = 1
                last_num = num
            if seq > longest_seq:
                longest_seq = seq
                
        return longest_seq
        
