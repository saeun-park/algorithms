class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        points = []
        points.append(0)
        points.append(gain[0])

        for i in range(len(gain)):
            points.append(sum(gain[0:i+1]))
        return max(points)