class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        Q = collections.deque([(sr, sc)])
        color = image[sr][sc]
        visit = set([])
        while Q:
            x, y = Q.popleft()
            image[x][y] = newColor
            if (x, y) in visit: continue
            visit.add((x, y))
            for i in range(4):
                nx, ny = x + d[i][0], y + d[i][1]
                if 0 <= nx < len(image) and 0 <= ny < len(image[0]) and image[nx][ny] == color:
                    Q.append((nx, ny))
        return image