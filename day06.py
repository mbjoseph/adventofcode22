#%%
with open("data/06.txt", "r") as input:
    data = input.read().replace("\n", "")

# n = 4  # part 1
n = 14  # part 2
for i in range(n, len(data)):
    chars = data[(i - n) : i]
    if len(set(chars)) == n:
        print(i)
        break
