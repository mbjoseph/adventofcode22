#%%
with open("data/02.txt", "r") as input:
    data = input.read()

# %%
games = [g for g in data.split("\n") if g != ""]

# %%
def decode_letter(letter):
    if letter in ["A", "X"]:
        return 0  # rock
    if letter in ["B", "Y"]:
        return 1  # paper
    if letter in ["C", "Z"]:
        return 2  # scissors


# rows are the moves of player 1, cols are the moves of player 2
# entries are the winner (0: draw, 1: p1 wins, 2:p2 wins)
outcome_matrix = [[0, 2, 1], [1, 0, 2], [2, 1, 0]]

outcome_scores = [3, 0, 6]  # draw, player 1 wins, player 2 wins

#%%
def score_game(input):
    player1 = decode_letter(input[0])
    player2 = decode_letter(input[2])
    winner = outcome_matrix[player1][player2]
    return 1 + player2 + outcome_scores[winner]


# %%
# part 1
sum([score_game(g) for g in games])


# %%
# part 2
def determine_move(player1, player2):
    potential_outcomes = outcome_matrix[player1]
    desired_outcome = [1, 0, 2][player2]  # x: lose, y: draw, z: win
    move = [i for i, o in enumerate(potential_outcomes) if o == desired_outcome]
    return move[0]


def score_part2(input):
    player1 = decode_letter(input[0])
    player2 = decode_letter(input[2])
    player2_move = determine_move(player1, player2)
    winner = outcome_matrix[player1][player2]
    return 1 + player2_move + outcome_scores[winner]


sum([score_part2(g) for g in games])
# %%
