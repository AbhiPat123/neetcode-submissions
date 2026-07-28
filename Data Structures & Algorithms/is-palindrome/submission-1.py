class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alpha = [chr_.lower() for chr_ in s if chr_.isalnum()]
        return s_alpha == s_alpha[::-1]