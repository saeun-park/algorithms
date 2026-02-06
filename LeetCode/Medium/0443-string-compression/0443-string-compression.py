class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        count = 1
        pos = 0 # 압축 후 배열에서 다음 글자 쓸 위치

        for i in range(1, n+1):
            if i < n and chars[i] == chars[i-1]:
                count += 1
            else:
                chars[pos] = chars[i-1]
                pos += 1

                if count > 1:
                    for c in str(count):
                        chars[pos] = c
                        pos += 1

                count = 1
        return pos
