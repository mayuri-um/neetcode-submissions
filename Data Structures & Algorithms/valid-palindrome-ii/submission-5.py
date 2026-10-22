class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False

            l += 1
            r -= 1
        return True