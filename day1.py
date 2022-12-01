#%%
with open("data/01.txt", "r") as input:
    data = input.read()

#%%
elves = data.split("\n\n")
calories_by_elf = [e.split("\n") for e in elves]
elf_sums = [sum([int(c) for c in cals if c != '']) for cals in calories_by_elf]

# %%
# part 1
max(elf_sums)

# part 2 (sum of top 3 elves)
sum(sorted(elf_sums)[-3:])

# %%
