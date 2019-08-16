"""Итак, дан палиндром(число, что одинаково читается
   в обе стороны) - это сумма всех чисел от 1 до 15,
   за исключением одного пропущенного. 
Определите, какое число было пропущено ?"""

suma = sum(range(1, 16))
entire_suma = suma
print('entire_suma(1,..,15) = ', suma)

for i in range(1, 16):
    suma -= i
    if ((str(suma)[0] == str(suma)[-1]) and (len(str(suma)) > 2) and (entire_suma - suma <= 15)):
        print('Final palindrome: ' + str(suma) + '\nexcess number = ' + str(i))
    else:
        suma += i
