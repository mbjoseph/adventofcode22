#%%
import re

with open("data/05.txt", "r") as input:
    data = input.read()


moves = [line for line in data.split("\n") if line.startswith("move")]


# parse initial stack config
raw = data.split("\n")[:9]

inverted = list(reversed(raw))

index_positions = [idx for idx, val in enumerate(inverted[0]) if val.isdigit()]

n_stacks = len(index_positions)


stacks = []
for i in range(n_stacks):
    stack = []
    for j in range(1, 9):
        char = inverted[j][index_positions[i]]
        if char.istitle():
            stack.append(char)
    stacks.append(stack)


# part 1
# for move in moves:
#     n_crates, src, dest = [int(d) for d in re.findall(r'\d+', move)]
#     for i in range(n_crates):
#         crate = stacks[src-1].pop()
#         stacks[dest-1].append(crate)

# stacks
# "".join([s[-1] for s in stacks])

# part 2
for move in moves:
    n_crates, src, dest = [int(d) for d in re.findall(r"\d+", move)]
    crates = stacks[src - 1][-n_crates:]
    del stacks[src - 1][-n_crates:]
    stacks[dest - 1] = stacks[dest - 1] + crates

"".join([s[-1] for s in stacks])
#%%
