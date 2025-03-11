# 벽 부수고 이동하기 2 (G3)
# 19:22~19:58 (36분)

'''
n, m, k = n개의 행에 m개의 숫자, 최단 경로로 이동하고 k번 만큼 벽을 부술 수 있음

'''
from collections import deque

n, m, k = map(int,input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[0 for _ in range(k+1)] for _ in range(m)] for _ in range(n)]

def bfs(r,c,b_cnt):
    q = deque()
    q.append([r,c,b_cnt])
    visited[r][c][b_cnt] = 1

    while q:
        r, c, b_cnt = q.popleft()

        if r == n-1 and c == m-1:
            return visited[r][c][b_cnt]

        for dr, dc in [[0,1],[1,0],[0,-1],[-1,0]]:
            nr, nc = r + dr, c + dc

            if 0<=nr<n and 0<=nc<m:

                if board[nr][nc] == 1 and b_cnt < k and visited[nr][nc][b_cnt+1] == 0:
                    visited[nr][nc][b_cnt+1] = visited[r][c][b_cnt] + 1
                    q.append([nr,nc,b_cnt+1])
                
                if board[nr][nc] == 0 and visited[nr][nc][b_cnt] == 0:
                    visited[nr][nc][b_cnt] = visited[r][c][b_cnt] + 1
                    q.append([nr,nc,b_cnt])

    return -1

print(bfs(0,0,0))