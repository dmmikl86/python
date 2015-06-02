"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    temp_list = []
    zeros = []
    res = []
    for elem in line:
        if elem == 0:
            zeros.append(elem)
        else:
            temp_list.append(elem)

    temp_list.extend(zeros)

    zeros = []
    per = 0
    while per < len(temp_list):
        if per != 0:
            if temp_list[per] == temp_list[per - 1]:
                res.append(temp_list[per] * 2)
                per += 1
                zeros.append(0)
            else:
                res.append(temp_list[per - 1])
        if per + 1 == len(temp_list):
            res.append(temp_list[per])
        per += 1
    res.extend(zeros)
    return res

print merge([8, 16, 16, 8, 8])