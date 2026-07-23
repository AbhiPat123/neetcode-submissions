class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # Maps a number to its index
        for i, num in enumerate(nums):
            diff = target - num
            
            # If we've already seen the number we need, we're done
            if diff in seen:
                return [seen[diff], i]
            
            # Otherwise, add the current number to our dictionary
            seen[num] = i
        