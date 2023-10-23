def fib(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fib(i-1) + fib(i-2)
num_lines = int(input())
for j in range(num_lines):
    user = int(input())
    print(f"{user} = {fib(user-1)}")