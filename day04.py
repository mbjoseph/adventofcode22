#%%
with open("data/04.txt", "r") as input:
    data = input.read()

pairs = [p for p in data.split("\n") if p != ""]


def get_range(pair):
    range1, range2 = [p.split("-") for p in pair.split(",")]
    min1, max1 = [int(r) for r in range1]
    min2, max2 = [int(r) for r in range2]
    return min1, max1, min2, max2


def containing_pair(pair):
    min1, max1, min2, max2 = get_range(pair)
    range1_in_2 = min1 >= min2 and max1 <= max2
    range2_in_1 = min2 >= min1 and max2 <= max1
    return range1_in_2 or range2_in_1


contains = [containing_pair(p) for p in pairs]


def overlaps(pair):
    min1, max1, min2, max2 = get_range(pair)
    overlap = range(max(min1, min2), min(max1, max2) + 1)
    return len(overlap) > 0


sum([overlaps(p) for p in pairs])

# %%
