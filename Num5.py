# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

from cmath import sqrt
import random
import math


X1 = round(random.uniform(-1000,1000),2)
Y1 = round(random.uniform(-1000,1000),2)

X2 = round(random.uniform(-1000,1000),2)
Y2 = round(random.uniform(-1000,1000),2)

F = round(sqrt((X2-X1)**2 + (Y2-Y1)**2).real,2)

print(f"A({X1}, {Y1}); B({X2}, {Y2}) -> {F}")