class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        nums_ext = []
        nums = list(set(nums))
        for num in nums:
            nums_ext.extend([num-1,num+1])

        return len(nums_ext)-len(set(nums_ext))