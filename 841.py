class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        unlockedRooms = [False for _ in range(len(rooms))]
        unlockedRooms[0] = True
        queue = collections.deque(rooms[0])
        roomNum = len(rooms) - 1
        while queue:
            key = queue.popleft()
            if not unlockedRooms[key]:
                roomNum -= 1
                unlockedRooms[key] = True
                for newkey in rooms[key]:
                    queue.append(newkey)
        if roomNum == 0:
            return True
        else:
            return False