number=str(input('Введите четырехзначное число: '))
if number[0]==number[-1] and number[1]==number[-2]:
    print('настоящее')
else:
    print('кривое')