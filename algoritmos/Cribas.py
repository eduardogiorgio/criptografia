def criba(n):
	esprimo = [True for i in range(0, n+1)]         #arreglo donde se guardaran los primos hasta n, iniciado en V
	for i in range(2,n+1):                          #recorrer a partir de 2.. hasta n (range no incluye el limite)
		if esprimo[i]:                          #esprimo[2..] es true
			for j in range(2*i, n+1, i):    # j a partir de 2*2.. hasta n de 2.. en 2..
				esprimo[j]=False        #pone en F los que no son primos
	return [i for i in range(2,n+1) if esprimo[i]]  #devuelve un arreglo con los primos en el rango de n
