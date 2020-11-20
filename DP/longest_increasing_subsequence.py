from bisect import bisect_left, bisect_right


def lis(a, strict=False):
    # Given an array, find a longest increasing (non-strict) subsequence (non-consecutive)
    # O(n log n)
    bisect = bisect_left if strict else bisect_right
    n = len(a)
    predecessor = [0]*n
    last_of_length = [0]*(n+1)

    l = 0
    for i in range(n):
        j = bisect([a[last_of_length[x]] for x in range(n+1)][1:l+1], a[i]) + 1
        new_l = j
        predecessor[i] = last_of_length[new_l-1]
        last_of_length[new_l] = i

        if new_l > l:
            l = new_l

    s = [0]*l
    k = last_of_length[l]
    for i in reversed(range(l)):
        s[i] = a[k]
        k = predecessor[k]

    return s


seq = [0, 0, 1]
print(lis(seq))
print(lis(seq, strict=True))
