def read_menu():
    items = int(input())
    name = input()
    list = [input() for i in range(items)] 
    if 'pea soup' in list and 'pancakes' in list:
        return name
    return -1

def parse_page():
    restaurants = int(input())
    for i in range(restaurants):
        res = read_menu()
        if res != -1:
            return res
    return "Anywhere is fine I guess"

res = parse_page()
print(res)
