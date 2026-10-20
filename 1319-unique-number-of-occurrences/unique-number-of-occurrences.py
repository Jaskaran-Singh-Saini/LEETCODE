class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        counts = defaultdict(int)
        for i in arr:
            counts[i] += 1
        occur = list(counts.values())

        return len(occur) == len(set(occur))