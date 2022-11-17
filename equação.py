import math
#Entrada
A = float(input("Qual o valor de A? "))
B = float(input("Qual o valor de B? "))
C = float(input("Qual o valor de C? "))
#Processamento Obrigatorio!
delta = B**2 -4*A*C
if delta<0:
    #Possivel saida
    print(f"Essa equação não tem resultados no conjunto dos numeros reais!")
else:
    if A == 0:
        #Possivel saida
        print(f"Essa não é uma equação do 2° Grau")
    else:
        if C == 0:
            soluçãoSemB = -B/A
            #Possivel saida
            print(f"A solução da equação é 0 e {soluçãoSemB}")
        else:
            if B==0:
                soluçãosemCPositiva = math.sqrt(-C/A)
                soluçãosemCNegativa = - math.sqrt(-C/A)
                #Possivel saida 
                print(f"A solução da equação é que x = {soluçãosemCNegativa} e {soluçãosemCPositiva}")
                    
            else:
                if delta ==0:
                    bascaraUnica = (-B+ math.sqrt(delta))/(2*A)
                    print(f"O resultado unico foi: {bascaraUnica}")
                else:
                    bascaraPositivo = (-B+ math.sqrt(delta))/(2*A)
                    bascaraNegativo = (-B- math.sqrt(delta))/(2*A)
                    #Saida principal
                    print(f"O resultado é que x = {bascaraPositivo} e {bascaraNegativo}")

             

    
    
