#4 Sabe-se que:1 pé = 12 polegadas, 1 jarda = 3 pés, 1 milha = 1.760 jardas. Faça um programa que obtém uma medida em pés, e faz as conversões a seguir, mostrando osresultados logo ao final.a) polegadasb) jardasc) milhas

valorPes = float(input("digite o valor em pes: "))
pol = valorPes / 12
jar =  valorPes / 3
milhas = valorPes/(1760 * 3) 

print("polegadas: "+str(pol)+"\n")
print("jardas: "+str(jar)+"\n")
print("milhas"+str(milhas)+"\n")