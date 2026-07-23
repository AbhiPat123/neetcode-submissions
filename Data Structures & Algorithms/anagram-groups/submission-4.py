from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        angrms_groups = defaultdict(list)

        for s in strs:

            counts = [0] * 26
            minus_val = ord('a')
            for ltr in s:
                counts[ord(ltr) - minus_val]+=1

            angrms_groups[tuple(counts)].append(s)

        return list(angrms_groups.values())
            
            

