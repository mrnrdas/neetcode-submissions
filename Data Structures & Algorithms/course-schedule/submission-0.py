from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def dfs(node):
            if node in visited:
                return False

            if node in seen:
                return True

            visited.add(node)

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            visited.remove(node)
            seen.add(node)
            return True

        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visited = set()
        seen = set()

        for course in range(numCourses):
            if course not in seen:
                if not dfs(course):
                    return False

        return True
        