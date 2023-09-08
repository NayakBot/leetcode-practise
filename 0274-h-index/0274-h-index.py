class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)
        n = len(citations)
        count = 0

        for i in range(n):
            if citations[n-i-1] > i:
                count += 1
            else:
                return count
        return count