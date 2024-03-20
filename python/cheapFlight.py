from typing import List

class Solution:
    def __init__(self, n: int, flight: List[List[int]], src: int, dst: int, k: int):
        self.n = n
        self.flight = flight
        self.src = src
        self.dst = dst
        self.k = k
        self.visited = {i: False for i in range(n)}
        self.edgeTo = {i: [] for i in range(n)}
        self.minPrice = float('inf')

        for x, y, z in flight:
            self.edgeTo[x].append((y, z))

    def findCheapFlight(self, place: int, count: int, sumPrice: int):
        if count > self.k + 1 or sumPrice >= self.minPrice:
            return

        if place == self.dst:
            self.minPrice = min(self.minPrice, sumPrice)
            return

        self.visited[place] = True

        for connectedPlace, flightFare in self.edgeTo[place]:
            if not self.visited[connectedPlace]:
                self.findCheapFlight(connectedPlace, count + 1, sumPrice + flightFare)

        self.visited[place] = False

    def get_min_price(self):
        self.findCheapFlight(self.src, 0, 0)
        return -1 if self.minPrice == float('inf') else self.minPrice

sol = Solution(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1)
print("Min Price:", sol.get_min_price())