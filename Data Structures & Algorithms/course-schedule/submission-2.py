from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Construct Adjacency list from array of edges
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        # Initialize a visited set
        visited = set()

        # DFS helper method
        def dfs(course):
            # If there is a cycle
            if course in visited:
                return False
            # If the array is empty then we have reached the end and can return True
            if graph[course] == []:
                return True

            # Add to the currently visited
            visited.add(course)
            # Loop through the neighbors aka prereq
            for prereq in graph[course]:
                # Recursivley run dfs on the prereq
                if not dfs(prereq):
                    return False
            # If no cycles we can remove from where we are visiting
            visited.remove(course)
            # If we never ran into a cycle we can assign the array as empty
            graph[course] = []
            # Return True if never ran into cycle
            return True

        # Check every course because unsure if graph is fully connected
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True