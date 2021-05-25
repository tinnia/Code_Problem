class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = [0] * len(rooms)
        Q = deque([(0)])
        while Q:
            x = Q.popleft()
            visit[x] = 1
            while rooms[x]:
                if visit[rooms[x][0]] == 0:
                    Q.append(rooms[x][0])
                rooms[x].remove(rooms[x][0])
        return False if visit.count(0) else True