def longest_sum_zero(a):
    # Given an array, find a longest sub-array (consecutive) with sum 0
    # O(n)
    res = (-1, -1)
    n = len(a)
    sum_to_pos = {0: 0}
    total = 0
    best = 0

    for i in range(1, n + 1):
        total += a[i - 1]
        if total in sum_to_pos:
            first_pos = sum_to_pos[total]
            opt = i - first_pos
            if opt > best:
                best = opt
                res = (first_pos, i)
        else:
            sum_to_pos[total] = i

    return res


test = [1, 4, 3, 6, -1, -1, -1, -3, -2, -6, 7, 8, 0, 0, 3, -5]
x = longest_sum_zero(test)
print(sum(test[x[0]:x[1]]))
