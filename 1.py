with open('input.txt') as f:
    n, m = map(int, f.readline().split())
    sides = {}
    for i in range(1, n+1):
        sides[i] = []
    for i in range(m):
        v1, v2 = map(int, f.readline().split())
        sides[v1].append(v2)
        sides[v2].append(v1)
    visited = [False] * (n+1)
    parent = {}
    u, v = map(int, f.readline().split())

cur_node = u
node_found = 1
node_completed = 0
while True:
    visited[cur_node] = True
    flag = False
    for i in sides[cur_node]:
        if i == v:
            print(1)
            exit()
        if not visited[i]:
            parent[i] = cur_node
            cur_node = i
            node_found += 1
            flag = True
            break
    if not flag:
        node_completed += 1
        if node_found == node_completed:
            break
        cur_node = parent[cur_node]
print(0)