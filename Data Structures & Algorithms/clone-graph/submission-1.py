"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        graph = {} 
        
        if not node:
            return None

        # dfs traversal on nodes to build graph 
        def dfs(node):
            if node in graph:
                return
            graph[node] = Node(node.val, None)
            for n in node.neighbors:
                dfs(n)
                graph[node].neighbors.append(graph[n])
                    
        dfs(node)
        return graph.get(node)