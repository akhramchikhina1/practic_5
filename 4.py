num = int(input("Введите число от 1 до 100: "))

if num == 1:
    print(num, "попугай")
elif 2 <= num <= 4:
    print(num, "попугая")
elif 5 <= num <= 20:
    print(num, "попугаев")
elif num % 10 == 1:
    print(num, "попугай")
elif num % 10 == 2 or num % 10 == 3 or num % 10 == 4:
    print(num, "попугая")
else:
    print(num, "попугаев")