from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = Counter(nums)
        
        return sorted(num_counts, key=lambda x:num_counts[x], reverse=True)[:k]