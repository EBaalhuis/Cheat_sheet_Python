def lcs(x, y):
    # Given two strings find the length of longest common subsequence (i.e. not consecutive!)
    # O(m*n)
    m = len(x)
    n = len(y)
    row1 = [0]*(n+1)

    for i in range(1, m+1):
        row2 = [0]*(n+1)
        for j in range(1, n+1):
            if x[i] == y[j]:
                row2[j] = row1[j-1] + 1
            else:
                row2[j] = max(row2[j-1], row1[j])
        row1 = row2

    return row2[m][n]
