class Solution:
    def isPalindrome(self, s: str) -> bool:
        itr1 = 0
        itr2 = len(s)-1
        while itr1<itr2:
            while not s[itr1].isalnum():
                itr1 += 1
            while not s[itr2].isalnum():
                itr2 -= 1
            if s[itr1].lower() != s[itr2].lower():
                return False
            itr1 += 1
            itr2 -= 1
        return True
