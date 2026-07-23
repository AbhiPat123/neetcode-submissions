from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        nums_set = set(nums)
        max_count = 0
        for num in nums:
            if num-1 not in nums_set:
                cur_num = num
                cur_count = 1
                # means we are at some start of sequence
                while (cur_num+1) in nums_set:
                    cur_num += 1
                    cur_count += 1

                max_count = max(max_count,cur_count)
        
        return max_count