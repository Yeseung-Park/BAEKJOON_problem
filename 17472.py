N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def DFS(i, j):
    island.append((i, j))
    visited[i][j] = 1
    for k in range(4):
        ni, nj = i+di[k], j+dj[k]
        if visited[ni][nj] or ni < 0 or ni >= N or nj < 0 or nj >= M:
            continue
        DFS(ni, nj)


# 섬 구분하기
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
visited = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if visited[i][j] or board[i][j] == 0:
            continue
        island = []
        DFS(i, j)
        print(island)

print(board)