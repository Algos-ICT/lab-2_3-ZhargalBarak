with open('input.txt') as f:
    N = int(f.readline())
    buses = [[] for _ in range(N+1)]
    d, v = map(int, f.readline().split())
    R = int(f.readline())
    for i in range(R):
        n1, t1, n2, t2 = map(int, f.readline().split())
        buses[n1].append((t1, n2, t2))

INF = float('inf')
Time  = [INF] * (N+1)
Time[d] = 0
visited = [False] * (N+1)
while True:
    min_time = INF
    for i in range(1, N+1):
        if not visited[i] and Time[i] < min_time:
            min_time = Time[i]
            min_village = i
    if min_time == INF:
        break
    n1 = min_village
    visited[n1] = True
    for t1, n2, t2 in buses[n1]:
        if Time[n1] <= t1 and t2 <= Time[n2]:
            Time[n2] = t2

with open('output.txt', 'w') as f:
    if Time[v] == INF:
        f.write('-1')
    else:
        f.write(str((Time[v])))