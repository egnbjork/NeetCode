class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0

        longest_seq = 1
        seq = 1

        for num in nums:
            seq_num = num
            while seq_num + 1 in nums:
                seq = seq + 1
                seq_num = seq_num + 1
                if seq > longest_seq:
                    longest_seq = seq
            seq = 1
                
        return longest_seq
        
