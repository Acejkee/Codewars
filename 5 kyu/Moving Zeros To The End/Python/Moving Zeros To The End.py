def move_zeros(array):
    zeros = []
    ans = []
    for i in array:
        if i != 0 or type(i) == bool:
            ans.append(i)
        elif i == 0:
            zeros.append(i)
    ans.extend(zeros)
    return ans
            