class Solution:
    def hIndex(self, citations: List[int]) -> int:

        sorted_citations = sorted(citations, reverse=True)
        h = 0
        i = 0
        n = len(citations)

        while i < n and sorted_citations[i] > h:
            h += 1
            i += 1

        return h