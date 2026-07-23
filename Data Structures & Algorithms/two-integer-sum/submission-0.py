class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        for idx,num in enumerate(nums):
            get_prev_idx = diff_dict.get(num)
            if get_prev_idx is None:
                diff_dict[target-num] = idx
            else:
                return [get_prev_idx, idx]