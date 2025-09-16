# Last updated: 9/16/2025, 2:16:19 PM
class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        g = []
        neighborCount = []
        currentLeaves = []
        nextLeaves = []
        
        def getTreeDiameter(edges):
            nonlocal g, neighborCount, currentLeaves, nextLeaves
            n = len(edges) + 1
            g.clear()
            neighborCount.clear()
            for _ in range(n):
                g.append([])
                neighborCount.append(0)
            for u, v in edges:
                g[u].append(v)
                g[v].append(u)
                neighborCount[u] += 1
                neighborCount[v] += 1

            currentLeaves.clear()
            nextLeaves.clear()
            for u, neighCnt in enumerate(neighborCount):
                if neighCnt == 1:
                    currentLeaves.append(u)
            
            result = 0
            while len(currentLeaves) > 1:
                result += 2
                for u in currentLeaves:
                    for v in g[u]:
                        neighborCount[v] -= 1
                        if neighborCount[v] == 1:
                            nextLeaves.append(v)
                currentLeaves, nextLeaves = nextLeaves, currentLeaves
                nextLeaves.clear()
            
            return result - (1 - len(currentLeaves))
        
        d1 = getTreeDiameter(edges1)
        d1h = (d1 + 1) // 2
        d2 = getTreeDiameter(edges2)
        d2h = (d2 + 1) // 2

        return max(d1, d2, 1 + d1h + d2h)
