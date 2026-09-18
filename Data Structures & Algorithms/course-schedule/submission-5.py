class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        edges = [[] for _ in range(numCourses)]

        for p, c in prerequisites:
            indegree[c] += 1
            edges[p].append(c)

        queue = deque() 

        for c in range(numCourses):
            if indegree[c] == 0:
                queue.append(c)
             
        visited = 0 # keeps track of courses completed
        while queue: # keeps track if queue is empty
            prereq = queue.popleft()
            for c in edges[prereq]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    queue.append(c)
            visited += 1

        return visited == numCourses