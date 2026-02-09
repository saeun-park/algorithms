class Solution:
    def removeStars(self, s: str) -> str:
        cnt = 0
        n = len(s)
        # start = 0
        li = list(s)
        stack = []

        for i in range(n):
            if li[i]!='*':
                stack.append(li[i])
            else:
                stack.pop()

        return "".join(stack)

