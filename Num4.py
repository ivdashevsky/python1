# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y)
import random

N = int(input("Введите номер четверти 2D-плоскости "))
X = round(random.uniform(0.01, 1000),2)
Y = round(random.uniform(0.01, 1000),2)

if not (N >= 1 and N <= 4):
    print("Введенный номер не соответствует номеру 2D-плоскости")
else:
    if (N == 1):
        X *=1
        Y *=1
        print(f"X = {X}, Y = {Y}")
    if (N == 2):
        X *=-1
        Y *=1
        print(f"X = {X}, Y = {Y}")
    if (N == 3):
        X *=-1
        Y *=-1
        print(f"X = {X}, Y = {Y}")
    if (N == 4):
        X *=1
        Y *=-1
        print(f"X = {X}, Y = {Y}")
    