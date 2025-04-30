family = tuple(['Миша', 'Рита', 'Таня', 'Эмилия', 'Амелия'])
print(f'''Первый элемент кортежа: {family[0]}
Последний элемент кортежа: {family[-1]}''')
print(family[1::2])
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
num = int(input('Введите число: '))
if num in numbers:
    numbers.remove(num)
else:
    numbers.add(num)
print(f'Длина множества: {len(numbers)}')
print(numbers)