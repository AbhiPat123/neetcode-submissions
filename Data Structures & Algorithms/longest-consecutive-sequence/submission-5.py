class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_ = list(set(nums))
        if len(nums_) == 0:
            return 0
        if len(nums_) == 1:
            return 1

        nums_ext = []
        for num in nums:
            nums_ext.extend([num-1,num+1])
        print(nums_ext)
        return len(nums_ext)-len(set(nums_ext))