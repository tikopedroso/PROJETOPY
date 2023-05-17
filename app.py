def main():
    print("Calcule o seu IMC:")
    peso = (input('Digite seu peso: '))
    altura = (input('Digite sua altura: '))   
   
    while not enumero(peso, altura):
        print("Favor digitar corretamente....")
        peso = input('Digite seu peso: ')
        altura = input('Digite sua altura: ')

    indices = TransformaTexto(peso, altura)    

    imc = CalcularIMC(indices[0],indices[1])     
    print(f"O IMC de Peso: {indices[0]:,.2f} e Altura: {indices[1]:,.2f} é: {imc:,.2f} - ", DefinirIMC(imc))   

#calcula o IMC 
def CalcularIMC(peso, altura):    
    IMC = peso/altura**2   
    return IMC

def DefinirIMC(IMC):    
    if(IMC < 18.5):
        return "MAGREZA"
    if(IMC < 24.9 ):
        return "NORMAL"
    if(IMC < 30):
        return "SOBREPESO" 
    else:
        return "OBESIDADE"

#Validando o valor digitado
def enumero(peso, altura):
    try:
        peso = peso.replace(",", ".")
        altura = altura.replace(",", ".")
        if float(peso) and float(altura):            
            return True
    except:
        pass
    return False

def TransformaTexto(peso, altura):
    peso = float(peso.replace(",","."))
    altura = float(altura.replace(",","."))    
    return peso, altura

main()