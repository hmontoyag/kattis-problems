def game():
    set = [1,2,3,4,5,6,7,8,9,10]
    while 1:
        num = int(input())
        if num == 0:
            exit()
        call = input()
        if call == 'too high':
            set = [x for x in set if x < num]
        if call == 'too low':
            set = [x for x in set if x > num]
        if call == 'right on':
            if len(set) > 0 and num in set:
                return 'Stan may be honest'
            return 'Stan is dishonest'

while 1:
    print(game())
