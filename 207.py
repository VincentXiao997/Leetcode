class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.buildGraph(prerequisites, numCourses)
        queue = collections.deque([])
        tokenCourses = 0
        for i in graph:
            if len(graph[i]) == 0:
                queue.append(i)
        while queue:
            course = queue.popleft()
            validCourses = self.findValidCourses(graph, course)
            for courseIndex in validCourses:
                queue.append(courseIndex)
            tokenCourses += 1
        if tokenCourses == numCourses:
            return True
        else:
            return False
    
    def findValidCourses(self, graph, course):
        validCourses = []
        for i in graph:
            if i == course:
                continue
            if course in graph[i]:
                graph[i].remove(course)
                if len(graph[i]) == 0:
                    validCourses.append(i)
        return validCourses
            
            
    def buildGraph(self, prerequisites, numCourses):
        graph = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        return graph
        