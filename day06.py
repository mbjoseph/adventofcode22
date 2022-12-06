#%%
with open("data/06.txt", "r") as input:
    data = input.read().replace("\n", "")


def solve(data, n):
    for i in range(n, len(data)):
        chars = data[(i - n) : i]
        if len(set(chars)) == n:
            return i


solve(data, 4)
solve(data, 14)
