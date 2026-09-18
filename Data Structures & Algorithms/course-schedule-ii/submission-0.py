class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        order = []

        indegree = [0] * numCourses
        adj_list = [[] for _ in range(numCourses)]

        for c, p in prerequisites:
            adj_list[p].append(c)
            indegree[c] += 1

        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
            
        visited = 0
        while queue:
            p = queue.popleft()
            for c in adj_list[p]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    queue.append(c)
            visited += 1
            order.append(p)

        if visited == numCourses:
            return order
        else:
            return []