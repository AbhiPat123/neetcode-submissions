from collections import Counter, defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = Counter(nums)
        
        freq_dict = defaultdict(list)
        for num in num_counts:
            freq_dict[num_counts[num]].append(num)
        ret_list = []
        for freq in range(max(freq_dict.keys()),0,-1):
            if k>=len(freq_dict.get(freq,[])):
                ret_list.extend(freq_dict.get(freq,[]))
                k = k-len(freq_dict.get(freq,[]))
            elif k>0:
                ret_list.extend(freq_dict.get(freq,[])[:k])
        return ret_list

                 

