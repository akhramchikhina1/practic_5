weight=float(input('Введите вес: '))
high=float(input('Введите рост: '))
imt_r=weight/((high/100) ** 2)
imt_r=round(imt_r,2)
if imt_r < 16:
    print('выраженный дефицит массы тела')
elif 16 <= imt_r <= 18.49:
    print('недостаточная масса тела')
elif 18.5 <= imt_r <= 24.99:
    print('норма')
elif 25 <= imt_r <= 29.99:
    print('избыточная масса тела')
elif 30 <= imt_r <= 34.99:
    print('ожирение первой степени')
elif 35 <= imt_r <= 39.99:
    print('ожирение второй степени')
elif imt_r >= 40:
    print('ожирение третьей степени')