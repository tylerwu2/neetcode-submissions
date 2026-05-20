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

        visited = set()
        # dfs traversal on nodes to build graph 
        def dfs(node):
            if node is None:
                return
            visited.add(node)
            graph[node] = Node(node.val, None)
            for n in node.neighbors:
                if n in visited:
                    graph[node].neighbors.append(graph[n])
                else:
                    dfs(n)
                    graph[node].neighbors.append(graph[n])
                    
        dfs(node)
        if len(graph) == 0:
            return None
        else:
            return list(graph.values())[0]