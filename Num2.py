# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

X = int(input('Введите X (0 или 1)'))
Y = int(input('Введите Y (0 или 1)'))
Z = int(input('Введите Z (0 или 1)'))

if (X not in [0,1] or Y not in [0,1] or Y not in [0,1]):
    print("Неверные значения входных переменных")
else: 
    F = (not(X or Y or Z) == (not X and not Y and not Z))
    print(F)
