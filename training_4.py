def move_zeros(lst):
    lst_new = []
    count_zeros = 0
    for el in lst:
        if el != 0:
            lst_new.append(el)
        else:
            count_zeros += 1
    for i in range(count_zeros):
        lst_new.append(0)
    return lst_new
