# Last updated: 9/16/2025, 2:17:17 PM
from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def min_swaps_to_sort(arr):
            # This function calculates the minimum number of swaps to sort the array
            n = len(arr)
            sorted_arr = sorted((val, i) for i, val in enumerate(arr))
            visited = [False] * n
            swaps = 0
            
            for i in range(n):
                if visited[i] or sorted_arr[i][1] == i:
                    continue
                
                # Find the cycle
                cycle_size = 0
                x = i
                while not visited[x]:
                    visited[x] = True
                    x = sorted_arr[x][1]
                    cycle_size += 1
                
                if cycle_size > 1:
                    swaps += cycle_size - 1
            
            return swaps
        
        if not root:
            return 0
        
        # Perform level order traversal
        queue = deque([root])
        total_swaps = 0
        
        while queue:
            level_size = len(queue)
            level_values = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Calculate swaps needed for the current level
            total_swaps += min_swaps_to_sort(level_values)
        
        return total_swaps
