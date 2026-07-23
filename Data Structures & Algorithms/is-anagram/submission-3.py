class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = [0] * 26
        minus_val = ord('a')
        for ltr in s:
            counts[ord(ltr) - minus_val]+=1
        # print(counts)

        for ltr in t:
            counts[ord(ltr) - minus_val]-=1
        # print(counts)
        return all([i==0 for i in counts])
        
        


