#2  Escreva um programa que recebe o salário base de um funcionário, calcula e mostra o salário areceber, sabendo-se que esse funcionário tem gratificação de 5% sobre o salário base e pagaimposto de 7% sobre o salário base.

salario = int (input("digite o salario: \n"))
gra = salario*0.05
imp = salario*0.07
print("Gratificação(5%): "+ str(gra)+"\n")
print("Imposto(7%): "+ str(imp)+"\n")
print("Salario com reajustes: "+str(salario+gra-imp)+"\n")