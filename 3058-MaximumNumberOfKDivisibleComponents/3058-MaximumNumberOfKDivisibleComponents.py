# Last updated: 9/16/2025, 2:16:39 PM
from collections import defaultdict

class Solution(object):
    def maxKDivisibleComponents(self, n, edges, values, k):
       
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        visited = [False] * n
        self.components = 0  
        def dfs(node):
            visited[node] = True
            subtree_sum = values[node]
            for neighbor in tree[node]:
                if not visited[neighbor]:
                    neighbor_sum = dfs(neighbor)
                    if neighbor_sum % k == 0:
                        self.components += 1
                    else:
                        subtree_sum += neighbor_sum

            return subtree_sum

        # Step 4: Start DFS from node 0
        dfs(0)
        if sum(values) % k == 0:
            self.components += 1
        return self.components
