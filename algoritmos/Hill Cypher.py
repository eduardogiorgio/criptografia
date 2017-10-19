#es requerida la libreria
#python -m pip install numpy
# documentacion de numpy
# https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.matrix.html
import numpy

diccionario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
modulo = len(diccionario)
# clave ccbe
clave = numpy.matrix([[3, 3],[2, 5]])

#matriz 2x2
# 4, 9, 13 y 18 HOLA

def checkear(texto):
    largo = len(texto)
    #checkea que el texto a sifrar sea multiplo de 2
    if(not(largo > 2 and (largo % 2) == 0)):
        exit("el texto no es multiplo de 2 y mayor a 0")
        
def obtenerNumeros(texto):
    valores =[]
    for i in texto:
        valor = diccionario.find(i)
        if(valor == -1):
            exit("el caracter:'"+i+"' no existe en el diccionario")
        valores.append(valor);
    return valores

def agruparColumna(valores):
    agrupaciones =[];
    for i in range(0,len(valores),2):
        agrupaciones.append(numpy.matrix([[valores[i]],[valores[i+1] ]]) % modulo )
    return agrupaciones

def obtenerTexto(arraytexto):
    texto =""
    for i in arraytexto:
                texto+= diccionario[int(i)];
    return texto

# revisar de poner todo en mayuscula y pasar el diccionario y sino uno por defecto
# tomo de a 2
def cifrar( texto  = "TEST"):

    checkear(texto)    
    valores =  obtenerNumeros(texto)
    agrupacion = agruparColumna(valores)
    
    valresEncriptados =[]
    for i in agrupacion:
        valorEncriptado =  (clave * i) % 26
        # porque es de 2 por 2 sino ir sumando
        valresEncriptados.append(valorEncriptado[0,0])
        valresEncriptados.append(valorEncriptado[1,0])
    return obtenerTexto(valresEncriptados)

def decifrar( texto = "RGHB"):
    checkear(texto)
    valores =  obtenerNumeros(texto)
    agrupacion = agruparColumna(valores)

    valresDesencriptados =[]
    # nose porque va el 3 va de cajon y desencripta bien
    claveDesencriptar = (numpy.linalg.det(clave) * clave.I)%26 *3  % 26
    for i in agrupacion:
        valorDesencriptado =  (claveDesencriptar * i) % 26
        valresDesencriptados.append(valorDesencriptado[0,0])
        valresDesencriptados.append(valorDesencriptado[1,0])
    return obtenerTexto(valresDesencriptados)
    

    
       
