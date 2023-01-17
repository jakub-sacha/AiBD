from typing import Union, List


class Matrix:
    def __init__(self, data: Union[tuple, List[list]], value: Union[int, float] = 0):
        if isinstance(data, tuple):
            m, n = data
            if m > 0 and n > 0:
                self.data = [[value for _ in range(m)] for _ in range(n)]
            else:
                raise ValueError("You cannot create a matrix with a non-positive number of columns or rows.")
        else:
            self.data = data

    def __mul__(self, other):
        if len(self.data[0]) == len(other.data) and len(self.data) == len(other.data[0]):
            new_matrix = []
            for row_1 in self.data:
                row = []
                for i in range(len(other.data[0])):
                    col_2 = [other.data[j][i] for j in range(len(other.data))]
                    row.append(sum([a * b for a, b in zip(row_1, col_2)]))
                new_matrix.append(row)
            return Matrix(new_matrix)
        else:
            raise ValueError(f"You cannot matrix multiply a {len(self.data)}x{len(self.data[0])} matrix"
                             f" by a {len(other.data)}x{len(other.data[0])} matrix.")
