#%%
from string import ascii_lowercase, ascii_uppercase

with open("data/03.txt", "r") as input:
    data = input.read()

# %%
sacks = [s for s in data.split("\n") if s != ""]
scores = {let: idx + 1 for idx, let in enumerate(ascii_lowercase + ascii_uppercase)}

# %%
# part 1
def score_sack(sack):
    breakpoint = len(sack) // 2
    first_compartment = sack[:breakpoint]
    second_compartment = sack[-breakpoint:]
    common_letter = set(first_compartment).intersection(set(second_compartment))
    return scores.get(list(common_letter)[0])


assert score_sack("vJrwpWtwJgWrhcsFMMfFFhFp") == 16
assert score_sack("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL") == 38

sum([score_sack(s) for s in sacks])

# %%
# part 2
group_scores = []
for i in range(0, len(sacks), 3):
    sets = [set(s) for s in sacks[i : (i + 3)]]
    common_letter = set.intersection(*sets)
    group_scores.append(scores.get(list(common_letter)[0]))

sum(group_scores)
# %%
