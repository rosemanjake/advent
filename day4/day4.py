import os

def get_input(file):
    f = open(f"{os.path.dirname(__file__)}\\{file}", "r")
    return f.read()

def get_numbers(input):
    return [int(num) for num in input.split("\n\n")[0].split(',')]

def get_boards(input):
    splits = input.split("\n\n")
    return [get_board_arr(splits[i]) for i in range(len(splits)) if not i == 0]

def get_board_arr(board_str):
    rows = []
    rows_strs = board_str.split("\n")
    for row in rows_strs:
        tokens = row.split(" ")
        rows.append([int(token) for token in tokens if not token == ''])
    return rows

def play_game(numbers, boards):
    drawn_numbers = []
    results = []
    winning_boards = []
    for number in numbers:
        drawn_numbers.append(number)
        if not len(drawn_numbers) >= 5:
            continue
        for board in boards:
            if board in winning_boards:
                continue
            winning_row = check_rows(drawn_numbers, board)
            winning_column = check_columns(drawn_numbers, board)
            if(winning_row):
                winning_boards.append(board)
                results.append(Result(board, drawn_numbers, winning_row, "row", len(drawn_numbers)))
            elif (winning_column):
                winning_boards.append(board)
                results.append(Result(board, drawn_numbers, winning_column, "row", len(drawn_numbers)))
    return results

def check_rows(numbers, board):
    for row in board:
        if set(row).issubset(set(numbers)):
            return row
    return False

def check_columns(numbers, board):
    for i in range(len(board)):
        column = [row[i] for row in board]
        if set(column).issubset(set(numbers)):
            return column
    return False

def get_score(winner, final_numbers):
    score = 0
    for row in winner:
        for num in row:
            if num in final_numbers:
                score += num
    return score

class Result:
    def __init__(self, a_board, a_drawn, a_winner, a_type, nums):
        self.board = a_board
        self.drawn = a_drawn
        self.winner = a_winner
        self.type = a_type
        self.count = nums
        self.unmarked = Result.get_unmarked(self)
        self.solution = Result.get_solution(self)
    
    @staticmethod
    def get_unmarked(self):
        unmarked = []
        for row in self.board:
            for num in row:
                if num not in self.drawn:
                    unmarked.append(num)
        return unmarked

    @staticmethod
    def get_solution(self):
        return sum(self.unmarked) * self.drawn[len(self.drawn) - 1]

input = get_input("day4.txt")
numbers = get_numbers(input)
boards = get_boards(input)
results = play_game(numbers, boards)
print(f"solution for part 1 = {results[0].solution}")
print(f"solution for part 2 = {results[len(results) - 1].solution}")