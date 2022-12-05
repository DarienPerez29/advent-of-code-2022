opponent_moves_vals = {
    "A": 1,
    "B": 2,
    "C": 3
}

player_moves_vals = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

final_score = 0

while True:
    line = input()
    curr_score = 0

    if line == "eof":
        break
    else:
        moves = line.split()
        opponent_move = opponent_moves_vals[moves[0]]
        player_move = player_moves_vals[moves[1]]

        curr_score += player_move

        if opponent_move == 1 and player_move == 3:  # Player loses
            pass
        elif (player_move > opponent_move
                or player_move == 1 and opponent_move == 3):  # Player wins
            curr_score += 6
        elif player_move == opponent_move:  # Draw
            curr_score += 3

        print(curr_score)
        final_score += curr_score

print(final_score)
