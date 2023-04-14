n = input("Введите шестизначный номер вашего билета:")
if len(n) == 6:
    s1 = int(n[0]) + int(n[1]) + int(n[2])
    s2 = int(n[3]) + int(n[4]) + int(n[5])
    if s1 == s2:
        print("Yes")
    else:
        print("No")
else:
    ("Неверно введен номер билета")
