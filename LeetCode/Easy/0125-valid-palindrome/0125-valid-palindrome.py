class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""

        for c in s:
            if c.isalnum():
                clean += c.lower()
        
        a, b = 0, len(clean)-1
        while a<b:
            if clean[a]==clean[b]:
                a += 1
                b -= 1
            else:
                return False
        return True
        