# Напишите программу, которая подсчитает и выведет сумму квадратов всех двузначных чисел, делящихся на 9.
# При решении задачи используйте комбинацию функций filter, map, sum.

# Обратите внимание: на 9 должно делиться исходное двузначное число, а не его квадрат.

value = [23, 63, 2, 81, 34, 234, 270]
value = filter(lambda x: (9 < x < 100) and (x%9 == 0), value)
value = map(lambda x: x**2, value)
print(sum(value))

## или

# komb = [x**2 for x in range(10,100) if not x%9]
# print(sum(komb)