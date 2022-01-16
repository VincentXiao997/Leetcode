def solution(arr):
    sortSet = {}
    for num in arr:
        sortSet[num] = sortSet.get(num, 0) + 1
    sortArr = [(sortSet[num], num) for num in sortSet]

    def sort(item):
        return (item[0], -item[1])

    sortArr = sorted(sortArr, key = sort, reverse=True)
    result = []
    for pair in sortArr:
        for _ in range(pair[0]):
            result.append(pair[1])
    return result

print(solution([5,5,2,1,3,3,3,4,4]))

print(solution([5,5,2,1,2,-1,-1,-1,-1,-2,-2]))
print(solution([1]))