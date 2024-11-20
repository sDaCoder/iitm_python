def minor_matrix(M, i, j):
    """
    Compute the "minor matrix"

    Arguments:
        M: list of lists
        i: integer
        j: integer
    Return:
        M_ij: list of lists
    """
    return [row[:j] + row[j+1:] for idx, row in enumerate(M) if idx != i]

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
i = 2
j = 0

print(minor_matrix(M, i, j))