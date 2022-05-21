def labirint(k, path, sides):
    room_cur = 1
    for i in range(k):
        colour = path[i]
        flag = False
        for vertex, side in sides[room_cur]:
            if side == colour:
                room_cur = vertex
                flag = True
                break
        if not flag:
            return 'INCORRECT'
    return str(room_cur)


with open('input.txt') as f:
    n, m = map(int, f.readline().split())
    sides = {}
    for i in range(1, n+1):
        sides[i] = []
    for _ in range(m):
        u, v, c = map(int, f.readline().split())
        sides[u].append([v, c])
        sides[v].append([u, c])
    k = int(f.readline())
    path = list(map(int, f.readline().split()))

with open('output.txt', 'w') as f:
    f.write(labirint(k, path, sides))