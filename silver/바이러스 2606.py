# 1번 : 컴퓨터 수
# 2번 : 직접 연결되어 있는 컴퓨터 수
# 3번 : 컴퓨터 연결 정보
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
# 그래프 초기화

graph = [[] for i in range(N + 1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    pass

# 방문 여부를 나타내는 리스트 초기화
visited = [False] * (N + 1)

# 1번 컴퓨터부터 시작하여 DFS 탐색 수행
dfs(graph, 1, visited)

# 방문한 노드 수 계산 (1번 컴퓨터 제외)
count = sum(visited) - 1

# 결과 출력
print(count)
