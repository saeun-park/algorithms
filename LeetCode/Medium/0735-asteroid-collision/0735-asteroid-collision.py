class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        stack = []

        for cur in asteroids:
            alive = True

            while stack and stack[-1] > 0 and cur < 0:
                if stack[-1] + cur < 0:
                    stack.pop()
                    continue
                elif stack[-1] == -cur:
                    stack.pop()
                    alive = False
                    break
                else:
                    alive = False
                    break
            
            if alive:
                stack.append(cur)

        return stack
