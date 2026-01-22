class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = {}

        for a in arr:
            counts[a] = counts.get(a, 0) + 1

        # len(counts) == len(set(counts.values()))
        return len(counts) == len(set(counts.values()))


        