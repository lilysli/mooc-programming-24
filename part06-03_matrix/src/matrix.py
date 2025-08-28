def read_matrix():
    matrix = []
    with open("matrix.txt") as f:
        for line in f:
            row = [int(x) for x in line.strip().split(",")]
            matrix.append(row)
    return matrix

def row_sums():
    matrix = read_matrix()
    return [sum(row) for row in matrix]

def matrix_sum():
    return sum(row_sums())

def matrix_max():
    matrix = read_matrix()
    return max(max(row) for row in matrix)