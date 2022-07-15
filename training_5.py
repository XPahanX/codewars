def zeros(n):
  '''Количество нулей в факториале числа'''
    count_zeros = 0
    five = 5
    while(five <= n):
        count_zeros += n // (five)
        five *= 5
    return count_zeros
