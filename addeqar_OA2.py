def solution(arr, target):
    hashSet = {}
    result = []
    for num in arr:
        if num in hashSet:
            if hashSet[num]:
                hashSet[target-num] = False
                hashSet[num] = False
                result.append([num, target-num])
        else:
            hashSet[target-num] = True
    return result

print(solution([5,2,3,3,1,2,3,-1,-2,4], 3))