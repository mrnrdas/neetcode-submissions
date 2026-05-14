from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        output = []
        visit, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True

            cycle.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return output
