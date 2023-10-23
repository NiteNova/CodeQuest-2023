cases = int(input())

for i in range (cases):
    x = int(input())
    websites = {}
    for _ in range(x):
        entry = input()
        sep = entry.split(" ")
        websites[sep[0]] = int(sep[1])
    for key, value in websites.items():
        if websites[key] >= 1000: 
            if '.lmco.com' not in key:
                print(key, value)
