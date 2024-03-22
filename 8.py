knuts = int(input("Введите количество кнатов: "))

galleons = knuts // (17 * 29)
sikles = (knuts - galleons * 17 * 29) // 29
knuts_secound = knuts - galleons * 17 * 29 - sikles * 29

result = ''
if galleons > 0:
    result += str(galleons) + " галлеонов "
if sikles > 0:
    result += str(sikles) + " сиклей "
if knuts_secound > 0:
    result += str(knuts_secound) + " кнатов"

print(result)