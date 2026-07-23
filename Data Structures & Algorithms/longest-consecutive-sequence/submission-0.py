class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_ext = []
        for num in nums:
            nums_ext.extend([num-1,num+1])

        return len(nums_ext)-len(set(nums_ext))