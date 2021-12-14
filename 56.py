class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        dict1 = {}
        list1 = set([])
        for a, b in intervals:
            if a in dict1:
                dict1[a] = max(dict1[a], b)
            else:
                dict1[a] = b
            list1.add(a)
        list1 = list(list1)
        list1.sort()
        # print(list1)
        i = 0
        results = []
        while i <len(list1):
            if i == len(list1):
                results.append([list1[i], dict1[list1[i]]])
                break
            start = list1[i]
            end = dict1[list1[i]]
            while i + 1 < len(list1) and end >= list1[i+1]:
                i += 1
                end = max(end, dict1[list1[i]])
            results.append([start, end])
            i += 1
        return results
            