import math


def solution(map, K):
    houses = []
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] == 1:
                houses.append([row, col])
    mapCopy = [[True if map[row][col] else False for col in range(len(map[row]))] for row in range(len(map))]
    return calculate(mapCopy, 0, 0, K, houses)


def calculate(mapCopy, x, y, K, houses):
    print(x, y)
    if mapCopy[x][y]:
        return
    mapCopy[x][y] = True
    # print(mapCopy)

    result = 0
    dis = calculateDistance(x, y, houses)
    if dis <= K:
        result += 1
    directions = [[-1, -1], [-1, 0], [-1, +1], [0, -1], [0, +1], [+1, -1], [+1, 0], [+1, +1]]
    for newX, newY in directions:
        tempX, tempY = x + newX, y + newY
        if tempX >= 0 and tempX < len(mapCopy) and tempY >= 0 and tempY < len(mapCopy[0]) and not mapCopy[tempX][tempY]:
            result += calculate(mapCopy, tempX, tempY, K, houses)
    return result



def calculateDistance(x, y, houses):
    distance = -math.inf
    for house in houses:
        dis = (abs(x - house[0]) + abs(y - house[1]))
        if dis > distance:
            distance = dis
    return distance



map = [[0,1], [0,0]]
print(solution(map, 3))
