#3 Escreva um programa que calcula e mostra a �rea de um c�rculo, uma vez que o usu�rioinforme o raio. Use math.pi para obter um valor aproximado de pi. (Use import math antes).
import math

raio = float(input("digite o raio: "))
area = math.pi * (raio ** 2)
print(area)