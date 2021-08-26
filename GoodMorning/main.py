cases = int(input())

rules = {
    1: [0,1,2,3,4,5,6,7,8,9],
    2: [0,2,3,5,6,8,9],
    3: [3,6,9],
    4: [0,4,5,6,7,8,9],
    5: [0,5,6,8,9],
    6: [6,9],
    7: [0,7,8,9],
    8: [0,8,9],
    9: [9],
    0: [0]
}

zero_blocked = [3,6,9]

def list_to_int(n):
    return int(''.join(map(str,n)))

def trial(low, high, eq, n):
    low = list_to_int(low)
    high = list_to_int(high)
    eq = list_to_int(eq)
    n = list_to_int(n)
    dict = {low: abs(low-n), high: abs(high-n), eq: abs(eq-n)}
    return min(dict, key=dict.get)

def first_greater(x,y):
    nl = rules[x]
    for i in nl:
        if i >= y:
            return i

def first_lower(x,y):
    nl = rules[x].copy()
    nl.reverse()
    for i in nl:
        if i <=y:
            return [x,i]
    return [x-1,9]

def allowed(n):
    if n[1] in rules[n[0]]:
        return list_to_int(n)

    else:
        if n[0] in zero_blocked:
            return trial(first_lower(n[0],n[1]), [n[0],first_greater(n[0],n[1])],[n[0],n[0]], n)
        else:
            return trial(first_lower(n[0],n[1]),[n[0],first_greater(n[0],n[1])],[n[0],n[0]], n)


for i in range(cases):
    target = [int(i) for i in input()] #[5,9]
    if len(target) == 1:
        print(target[0])

    elif len(target) == 3:
        hdth = target.pop(0)
        if target[0] == 0:
            if target[1] > 4:
                target =  110
            else:
                target = hdth*100
        else:
            target = allowed(target)
            target = target + (hdth*100)
        print(target)

    elif len(target)==2:
        target = allowed(target)
        print(target)
