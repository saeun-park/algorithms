class Solution:
    def reverse(self, x: int) -> int:
        int_min, int_max = -2**31, 2**31-1
        minus = -1 if x<0 else 1

        to_str = str(abs(x))
        to_str = to_str[::-1]
        res = int(to_str)*minus

        if res<int_min or res>int_max: return 0

        return res

        