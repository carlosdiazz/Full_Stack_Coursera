import random,os
os.system("clear")

print(4**2)

def aleatorio(nume):
    if nume ==1:
        return '{:02}'.format(random.randint(0,99))
    elif nume == 2:
        return '{:02},{:02}'.format(random.randint(0,99),random.randint(0,99))
    else:
        return '{:02},{:02},{:02}'.format(random.randint(0,99),random.randint(0,99),random.randint(0,99))

numero=int(input("Ingrese un numero para convertir: "))

def binario(nume):
    final=[]
    if nume == 0:
        return 0
    else:
        while nume>0:
            bina=nume%2
            nume=nume//2
            final.append(bina)
        final.reverse()
        return "".join(map(str, final))
            
def encriptar(lista):

    inicial="===-=====-=====-===="
    for i in lista:
        if i == str(1):
            inicial=inicial+"="
        else:
            inicial=inicial+"-"

    return inicial

def desencriptar(lista):
    nueva=lista[20:]
    final=""
    for i in nueva:
        
        if i == "=":
            final=final+"1"
        else:
            final=final+"0"
    return final


bina=binario(numero)

print("-----------------------------------------------------------------")
print(f"Uste ingreso el numero {numero} en binario es: {bina}")

print("-----------------------------------------------------------------")
print("Aqui esta encriptado en la linea: ")
encriptado=encriptar(bina)
print(encriptado)

print("-----------------------------------------------------------------")
print("Aqui se esta desencripto la linea: ")
desen=desencriptar(encriptado)
print(desen)