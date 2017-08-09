# convert the temperature to C or F
def to_c(temp):
    C =5/9*(temp-32)
    C=round(C,1)
    return(C)

def to_f(temp):
    F = 32+5/9*(temp)
    F=round(F,1)
    return(F)

