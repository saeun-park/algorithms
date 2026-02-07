class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = ["a", "e", "i", "o", "u"]
        n = len(s)
        cnt = 0
        res = 0
        word = s[0:k]
        for w in word:
            if w in vowel:
                cnt += 1
        res = cnt

        for i in range(n-k):
            if s[i+k] in vowel:
                cnt += 1
            if s[i] in vowel:
                cnt -= 1
            
            res = max(res, cnt)
            
        return res

        