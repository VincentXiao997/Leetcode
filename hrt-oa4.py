def solution(A):
    if not A:
        return 0
    mask = 1
    nextMask = mask << 1
    maxSubsetSize = 0
    toBeContinue = True
    while toBeContinue:
        subsetSize = 0
        toBeContinue = False
        for num in A:
            if nextMask < num:
                toBeContinue = True
            print(num, mask, num & mask)
            if num & mask:
                subsetSize += 1
        print(subsetSize)
        maxSubsetSize = max(maxSubsetSize, subsetSize)
        mask = nextMask
        nextMask = nextMask << 1
    return maxSubsetSize

print(solution([16, 16]))