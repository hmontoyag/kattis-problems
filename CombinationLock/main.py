def to_deg(n):
    return n*9

def clockwise_distance(curr, target):
    #0 ---- 39
    i = 0
    while curr != target:
        i+=1
        curr -= 1
        if curr < 0:
            curr = 39
    return i

def counterclck_distance(curr, target):
    i = 0
    while curr != target:
        i+=1
        curr+=1
        if curr >39:
            curr = 0
    return i
while flag == 0:
    line = list(map(int, input().split()))
    if line[0] == 0 and line[1] == 0 and line[2] == 0 and line[3] == 0:
        exit()
    else:
        total = 360 * 2 #initial two turns
        total += to_deg(clockwise_distance(line[0], line[1])) #first combination
        total += 360 #one full turn
        total += to_deg(counterclck_distance(line[1],line[2])) #second num
        total += to_deg(clockwise_distance(line[2], line[3]))
        print(total)
