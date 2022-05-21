with open('input.txt') as f:
    N, M = map(int, f.readline().split())
    field = []
    for i in range(N):
        field.append(f.readline()[:M])

visited = [[False for _ in range(M)] for _ in range(N)]

count = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            if field[i][j] == '#':
                count += 1
                stack = [(i, j)]
                while len(stack) != 0:
                    x, y = stack.pop()
                    if field[x][y] == '#' and not visited[x][y]:
                        visited[x][y] = True
                        if x != 0:
                            stack.append((x-1, y))
                        if x != N-1:
                            stack.append((x+1, y))
                        if y != 0:
                            stack.append((x, y-1))
                        if y != M-1:
                            stack.append((x, y+1))

with open('output.txt', 'w') as f:
    f.write(str(count))