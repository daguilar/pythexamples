def ImprimePalabra(sPalabra):
    for iRecorre in sPalabra:
        print (iRecorre)

def ReversaPalabra(Palabra):
    palabra_retorno = ''
    for iRecorre in Palabra:
        palabra_retorno = iRecorre + palabra_retorno
    return palabra_retorno

#inicio Main

PalabraIngresada = 'Holanda'
ImprimePalabra(PalabraIngresada)
print(ReversaPalabra(PalabraIngresada))