# 1번 : 컴퓨터 수
# 2번 : 직접 연결되어 있는 컴퓨터 수
# 3번 : 컴퓨터 연결 정보

def dfs(graph: list, ):
    pass

def bfs():
    pass

import sys
# N = 정점수, M = 간선수, V = 정점 번호
N, M, V = map(int, sys.stdin.readline().split())

# 그래프 제작 List의 인덱스와 정점넘버를 맞추기 위해서 N + 1을 한다.
graph = [[] for i in range(N + 1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 순서 , if vist[i] == 0일 경우에만 순서 업데이트 하는 형식으로
vist = [0] * (N + 1)
# DFS, BFS 출력


# for i in range()