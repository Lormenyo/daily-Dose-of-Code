class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:

        edges = {(a,b) for a,b in connections}

        neighbors = {city:[] for city in range(n)}

        edgeChanges = 0

        visited = set()

        for a,b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        def dfs(city):
            nonlocal edgeChanges

            for neighbor in neighbors[city]:
                if neighbor in visited:
                    continue
                if (neighbor, city) not in edges:
                    edgeChanges += 1
                
                visited.add(neighbor)
                dfs(neighbor)

        visited.add(0)
        dfs(0)
        return edgeChanges