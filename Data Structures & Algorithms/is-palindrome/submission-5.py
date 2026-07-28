class Solution:
    def isPalindrome(self, s: str) -> bool:
        itr1 = 0
        itr2 = len(s)-1
        while itr1<itr2:
            sitr1 = s[itr1]
            sitr2 = s[itr2]
            if sitr1.isalnum() and sitr2.isalnum():
                if sitr1.lower() != sitr2.lower():
                    return False
                else:
                    itr1 += 1
                    itr2 -= 1
            else:
                if not sitr1.isalnum():
                    itr1 += 1
                if not sitr2.isalnum():
                    itr2 -= 1
        return True
