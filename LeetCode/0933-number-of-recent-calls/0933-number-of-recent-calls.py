from collections import deque
class RecentCounter:

    def __init__(self):
        # 필요한 변수 초기화 -- 상태를 저장할 자료구조 초기화
        self.q = deque()    

    def ping(self, t: int) -> int:
        self.q.append(t)

        while self.q[0] < t-3000:
            self.q.popleft()
        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)