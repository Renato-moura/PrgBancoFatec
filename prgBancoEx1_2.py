#2  Escreva um programa que recebe o sal�rio base de um funcion�rio, calcula e mostra o sal�rio areceber, sabendo-se que esse funcion�rio tem gratifica��o de 5% sobre o sal�rio base e pagaimposto de 7% sobre o sal�rio base.

salario = int (input("digite o salario: \n"))
gra = salario*0.05
imp = salario*0.07
print("Gratifica��o(5%): "+ str(gra)+"\n")
print("Imposto(7%): "+ str(imp)+"\n")
print("Salario com reajustes: "+str(salario+gra-imp)+"\n")