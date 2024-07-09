r, c = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(r)]
def kkk(matrix):
    max_lengths = [max(map(len, map(str, col))) for col in zip(*matrix)]
    for row in matrix:
        formatted_row = [f"{num:>{length}}" for num, length in zip(row, max_lengths)]
        print(" ".join(formatted_row))

kkk(matrix)
