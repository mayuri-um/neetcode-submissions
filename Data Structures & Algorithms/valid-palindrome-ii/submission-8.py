class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l,s):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

            
        left, right = 0, lens(s) - 1
        while left < right:
            if s[left] != s[right]:
                return isPalindrome(left +1, right) or isPalindorm(left, right -1)
            left += 1
            right -= 1
        return True