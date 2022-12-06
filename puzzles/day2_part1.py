class Node():
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyCircularLinkedList():
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
            self.head.prev = self.head
        else:
            new_node = Node(data)
            last = self.head

            while last.next != self.head:
                last = last.next

            last.next = new_node
            new_node.prev = last
            new_node.next = self.head
            self.head.prev = new_node

    def getCurrentMoveData(self, my_move):
        curr_move = self.head

        while curr_move.data != my_move:
            curr_move = curr_move.next

        return curr_move


moves_list = DoublyCircularLinkedList()
moves_list.append(1)  # Rock
moves_list.append(2)  # Paper
moves_list.append(3)  # Scissors

opponent_moves_vals = {
    "A": 1,  # Rock
    "B": 2,  # Paper
    "C": 3  # Scissors
}

player_moves_vals = {
    "X": 1,  # Rock
    "Y": 2,  # Paper
    "Z": 3  # Scissors
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

        player_move_data = moves_list.getCurrentMoveData(player_move)
        if opponent_move == player_move_data.prev.data:  # Wins
            curr_score += 6
        elif opponent_move == player_move_data.data:  # Loses
            curr_score += 3

        final_score += curr_score

print(final_score)
