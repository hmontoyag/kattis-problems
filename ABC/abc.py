from sys import stdin

x, y, z = map(int,stdin.readline().split())
list = [x,y,z]
list.sort()
dict = {"A": list[0], "B": list[1], "C": list[2]}
order = stdin.readline().rstrip()
for i in order:
    print(dict[i], end=' ')
