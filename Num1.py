# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
N = int(input('Введите день недели '))
if (N >= 6 and N <= 7):
    print('Да')
elif (N >= 1 and N <= 5):
    print('Нет')
else: 
    print('Число вне диапозона недели')