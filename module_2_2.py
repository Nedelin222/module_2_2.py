print("Введите три целых числа: ")
first = int(input('1: '))
second = int(input('2: '))
third = int(input('3: '))
if first == second and second == third:
    print('3')
elif first == second or second == third or first == third:
    print('2')
else:
    print('0')