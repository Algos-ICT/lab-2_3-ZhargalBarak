def dfs(u):
    global visited, parent, sides, order
    cur_node = u
    visited[cur_node] = True
    node_found = 1
    node_completed = 0
    while True:
        flag = False
        for i in sides[cur_node]:
            if i not in visited:
                parent[i] = cur_node
                cur_node = i
                visited[cur_node] = True
                order.append(cur_node)
                node_found += 1
                flag = True
                break
        if not flag:
            node_completed += 1
            if node_found == node_completed:
                break
            cur_node = parent[cur_node]
    order.append(u)

def dfsTranspon(u):
    global visited, parent, sides_trans, count
    cur_node = u
    visited[cur_node] = True
    node_found = 1
    node_completed = 0
    while True:
        flag = False
        for i in sides_trans[cur_node]:
            if i not in visited:
                parent[i] = cur_node
                cur_node = i
                visited[cur_node] = True
                node_found += 1
                flag = True
                break
        if not flag:
            node_completed += 1
            if node_found == node_completed:
                break
            cur_node = parent[cur_node]

with open('input.txt') as f:
    n, m = map(int, f.readline().split())
    sides = {}
    sides_trans = {}
    for i in range(1, n+1):
        sides[i] = []
        sides_trans[i] = []
    for i in range(m):
        v1, v2 = map(int, f.readline().split())
        sides[v1].append(v2)
        sides_trans[v2].append(v1)

order = []
visited = {}
parent = {}
for u in sides:
    if u not in visited:
        dfs(u)

visited = {}
parent = {}
order = order[::-1]
count = 0
for u in order:
    if u not in visited:
        dfsTranspon(u)
        count += 1
print(count)