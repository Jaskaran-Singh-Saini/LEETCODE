class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        grph = defaultdict(list)

        for frm, to in tickets:
            grph[frm].append(to)

        for curr in grph:
            grph[curr].sort()

        itinerary = []

        def dfs(curr):
            dest = grph[curr]

            while dest:
                nxt = dest.pop(0)
                dfs(nxt)

            itinerary.append(curr)

        dfs('JFK')

        return itinerary[::-1]