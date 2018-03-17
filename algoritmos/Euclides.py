def mcd(eme,ene):
    if ene==0:
        return eme
    else:
        return mcd(ene, eme%ene)
