class Solution:
    def isPalindrome(self, s: str) -> bool:
        l , r = 0, len(s)-1
        while l < r:
            while l < r and not self.isalnm(s[l]):
                l += 1
            while r>l and not self.isalnm(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True   


     

    def isalnm(self, word):
        return (ord('A') <= ord(word) <= ord('Z') or
                ord('0') <= ord(word) <= ord('9') or
                ord('a') <= ord(word) <= ord('z'))


