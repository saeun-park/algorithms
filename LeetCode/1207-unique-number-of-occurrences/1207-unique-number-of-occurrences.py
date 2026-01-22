class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = {}

        for a in arr:
            counts[a] = counts.get(a, 0) + 1

        return len(counts) == len(set(counts.values()))