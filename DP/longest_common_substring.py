def lcs(s, t):
    # Given two strings find a longest common substring (i.e. consecutive!)
    # O(m*n)
    m = len(s)
    n = len(t)
    row1 = [0]*n
    best = 0
    res = ""

    for i in range(m):
        row2 = [0]*n
        for j in range(n):
            if s[i] == t[j]:
                if i == 0 or j == 0:
                    row2[j] = 1
                else:
                    row2[j] = row1[j-1] + 1
                if row2[j] > best:
                    best = row2[j]
                    res = s[i - best + 1: i + 1]
        row1 = row2
    return res
