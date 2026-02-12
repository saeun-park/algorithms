class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        n = len(s)
        repeat, string = 0, ""

        for ch in s:
            if ch.isdigit():
                repeat = repeat*10 + int(ch)
            elif ch == '[':
                stack.append((repeat, string))
                repeat, string = 0, ""
            elif ch == ']':
                prev_repeat, prev_string = stack.pop()
                string = prev_string + string*prev_repeat
            
            else: # 알파벳을 만나면
                string += ch

        return string


