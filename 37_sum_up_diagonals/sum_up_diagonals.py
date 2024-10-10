def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    size = len(matrix)
    total_sum = 0

    for i in range(size):
        total_sum += matrix[i][i]
        total_sum += matrix[i][size - 1 - i]
    if size % 2 == 1:
        total_sum -= matrix[size // 2][size // 2]
    return total_sum