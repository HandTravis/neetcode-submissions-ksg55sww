class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create an adjacency list for the prerequisites
        preqs = {i: [] for i in range(numCourses)}
        
        for course, prereq in prerequisites:
            preqs[course].append(prereq)
        
        visited = set()
        path = set()
        
        def dfs(course):
            if course in path:  # Cycle detected
                return False
            if course in visited:  # Already processed node
                return True
            
            # Mark the course as being visited in the current path
            path.add(course)
            
            # Perform DFS on all prerequisites of the current course
            for prereq in preqs[course]:
                if not dfs(prereq):
                    return False
            
            # Remove from the current path and mark as fully processed
            path.remove(course)
            visited.add(course)
            
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
