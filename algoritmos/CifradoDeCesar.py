def CifrarSinCesar(msj,dsp):                                                                    #msj= mensaje a cifrar; dsp= desplazamiento (entero+-)
    abc='abcdefghijklmnñopqrstuvwxyz '                                                          #alfabeto
    return ''.join([(abc[abc.find(msj.lower()[i])-(dsp%len(abc))]) for i in range(len(msj))])
