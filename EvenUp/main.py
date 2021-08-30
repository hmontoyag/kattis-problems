n = int(input())
res = []
deck = list(map(int, input().split()))

for i in range(n):
    card = deck[i]
    if len(res) != 0 and (card + res[len(res)-1]) % 2 == 0:
        res.pop()
    else:
        res.append(card)
print(len(res))
