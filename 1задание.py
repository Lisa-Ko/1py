number = int(input('Введите трехзначное число: '))
sum = 0
while number // 1000 > 0 :   
    if number//1000 > 0:
        print('Число не трехзначное')
        number = int(input('Введите трехзначное число: '))
while number / 10 > 0:
    sum = sum + number % 10
    number //= 10
print("Сумма чисел трехзначного числа равно:", sum)