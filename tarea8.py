#Actividad 1

def factorial(num):
    if num!=0:
        return num*factorial(num-1)
    else:
        return 1
num = int(input("Introdusca algun numero: "))
print(factorial(num))

#Actividad 2

def fibonacci(num):
    if num == 0:
      return 0
    if num == 1:
        return 1
    else:
        return fibonacci (num-1) + fibonacci(num-2) 
num=int(input("Introdusca algun numero: "))
print(fibonacci(num))
print("---------------------------------------")

#Actividad 3

def InvCad(cade):
    if len(cade)==0:
        return cade
    else:
        return InvCad(cade[1:])+cade[0]    
cade=str(input("Introdusca alguna cadena de caracteres: "))
print(InvCad(cade))
print("---------------------------------------")

#Actividad 4

def potencia(ba, expon):
    if expon==0:
        return 1
    else:
        ba*potencia(ba, expon-1)
        return ba*potencia(ba, expon-1)

ba=int(input("Introdusca algun valor al numero base: "))
expon=int(input("Introdusca algun valor a el exponente: "))
print(potencia(ba, expon))
print("---------------------------------------")

#Actividad 5

def SumDig(num):
    if num == 0:
        return 0
    else:
        return num % 10 + SumDig(num // 10)
num=int(input("Introdusca algun numero: "))
print(SumDig(num))
print("---------------------------------------")

#Actividad 6
def MerSor(list):
    if len(list) > 1:
        mit = len(list) // 2
        izquier= list[:mit]
        dere = list[mit:]

        MerSor(izquier)
        MerSor(dere)

        i = j = k = 0

        while i < len(izquier) and j < len(dere):
            if izquier[i] < dere[j]:
                list[k] = izquier[i]
                i += 1
            else:
                list[k] = dere[j]
                j += 1
            k += 1

        while i < len(izquier):
            list[k] = izquier[i]
            i += 1
            k += 1

        while j < len(dere):
            list[k] = dere[j]
            j += 1
            k += 1
list = [40, 33, 22, 13, 36, 4, 24]
MerSor(list)
print("Lista ordenada:", list)
print("---------------------------------------")

#Actividad 7

def QuiSor(list):
    if len(list) <= 1:
        return list
    else:
        pivo = list[len(list) // 2]
        izquier = [x for x in list if x < pivo]
        cent = [x for x in list if x == pivo]
        dere = [x for x in list if x > pivo]
        return QuiSor(izquier) + cent + QuiSor(dere)
list = [40, 33, 22, 13, 36, 4, 24]
ListOrd = QuiSor(list)
print("Lista ordenada:", ListOrd)
print("---------------------------------------")

#Actividad 8

def BusqBin(list, objeti, inic=0, fin=None):
    if fin is None:
        fin = len(list) - 1

    if inic > fin:
        return False

    med = (inic + fin) // 2

    if list[med] == objeti:
        return True
    elif list[med] > objeti:
        return BusqBin(list, objeti, inic, med - 1)
    else:
        return BusqBin(list, objeti, med + 1, fin)
ListOrd = [4, 13, 22, 24, 33, 36, 40]
objeti = 24
encont = BusqBin(ListOrd, objeti)
print(f"Este elemento {objeti} {'fue encontrado' if encont else 'no fue encontrado'} en esta lista.")
print("---------------------------------------")

#Actividad 9

def DivMatr(matr):
    num = len(matr)
    mit = num // 2
    B11 = matr[:mit, :mit]
    B12 = matr[:mit, mit:]
    B21 = matr[mit:, :mit]
    B22 = matr[mit:, mit:]
    return B11, B12, B21, B22
matr=([[3,9], [8,4]])
print(DivMatr(matr))
print("---------------------------------------")

#Actividad 10

def MultMatr(A, B):
    num = len(A)
    
    if num == 1:
        return A * B
    
    A11, A12, A21, A22 = DivMatr(A)
    B11, B12, B21, B22 = DivMatr(B)
    
    C11 = MultMatr(A11, B11) + MultMatr(A12, B21)
    C12 = MultMatr(A11, B12) + MultMatr(A12, B22)
    C21 = MultMatr(A21, B11) + MultMatr(A22, B21)
    C22 = MultMatr(A21, B12) + MultMatr(A22, B22)
    
    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
    return C

A = np.array([[3, 9], [2, 5]])
B = np.array([[8, 4], [6, 7]])
C = MultMatr(A, B)
print("Resultado de esta multiplicación de matrices:")
print(C)

def DivMatrz(matr):
    num = len(matr)
    mit = num // 2
    A11 = matr[:mit, :mit]
    A12 = matr[:mit, mit:]
    A21 = matr[mit:, :mit]
    A22 = matr[mit:, mit:]
    return A11, A12, A21, A22

def MultMatr(A, B):
    num = len(A)
    
    if num == 1:
        return A * B
    
    A11, A12, A21, A22 = DivMatr(A)
    B11, B12, B21, B22 = DivMatr(B)
    
    C11 = MultMatr(A11, B11) + MultMatr(A12, B21)
    C12 = MultMatr(A11, B12) + MultMatr(A12, B22)
    C21 = MultMatr(A21, B11) + MultMatr(A22, B21)
    C22 = MultMatr(A21, B12) + MultMatr(A22, B22)
    
    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
    return C

def MatrIdent(num):
    return np.eye(num)

def PotenMatr(matr, exponen):
    if exponen == 0:
        return MatrIdent(len(matr))
    elif exponen == 1:
        return matr
    
    mit = exponen // 2
    MitPoten = PotenMatr(matr, mit)
    
    if exponen % 2 == 0:
        return MultMatr(MitPoten, MitPoten)
    else:
        return MultMatr(MultMatr(MitPoten, MitPoten), matr)

A = np.array([[3, 6], [5, 2]])
exponen = 4
result = PotenMatr(A, exponen)
print(f"Resultado al elevar esta matriz a la potencia {exponen}:")
print(result)