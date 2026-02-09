# from collections import Counter
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        start = 0
        rq, dq = [], []
        # 문자열 말고 인덱스를 저장함.
        for i in range(n):
            if senate[i]=='R': rq.append(i)
            else: dq.append(i)

        while rq and dq:
            ridx, didx = rq.pop(0), dq.pop(0)

            if ridx < didx:
                rq.append(ridx+n)
            else:
                dq.append(didx+n)
        if rq:
            return "Radiant"
        else:
            return "Dire"
        