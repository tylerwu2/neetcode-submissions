class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # graph with prerequisites as the edges and courses as the nodes

        visited = set() # store current dfs path

        # adjacency list to build prerequisites conections
        edges = [[] for _ in range(numCourses)]

        for p in prerequisites:
            edges[p[0]].append(p[1]) # adds edge from course p[0] to course p[1]

        # traverse course graph, DFS/BFS, topological sort

        def dfs(course):
            if course in visited:
               return False
            if edges[course] == []:
                return True
            
            visited.add(course)
            for p in edges[course]:
                if not dfs(p): # run dfs on each prerequisite
                    return False
            visited.remove(course)
            edges[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        