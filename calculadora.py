import math

print("============")
print("alayomas'")
print("  math utils")
print("   v1.5")
print("============")


def divisores(n1):  # Divisores
    resdiv = list()
    td = 0
    n1 = int(n1)
    for td in range(1, n1 + 1):
        if (n1 % td == 0):
            resdiv.append(td)
    return resdiv


def multiplos(n1, nm):  # Múltiplos
    resmul = list()
    for i in range(1, nm + 1):
        resmul.append(n1 * i)
    return resmul


def listavertices(n1, n2):  # ListaVértices
    resle = list()
    for i in range(n1, n2 + 1):
        resle.append(i)
    return resle


def mmc(n1, n2, nm=256):  # MMC
    mn1 = multiplos(n1, nm)
    mn2 = multiplos(n2, nm)
    for i in mn1:
        if i in mn2:
            return i
    return mmc(n1, n2, nm=nm * 2)


def mdc(n1, n2):  # MDC
    dn1 = divisores(n1)
    dn1.reverse()
    dn2 = divisores(n2)
    for i in dn1:
        if i in dn2:
            return i
    return -1


def potencia(n1, n2):  # Potência
    respot = int(math.pow(n1, n2))
    return respot


def subtracao(*args):  # Subtração
    ressub = 0
    tamanho = len(subLS)
    i = 2
    ressub = subLS[0] - subLS[1]
    while i < tamanho:
        ressub -= subLS[i]
        i += 2
    return ressub


def divisao(*args):  # Divisão
    resdivi = 0
    tamanho = len(divLS)
    i = 2
    resdivi = divLS[0] / divLS[1]
    while i < tamanho:
        resdivi /= divLS[i]
        i += 2
    return resdivi


def reverso(revLS):  # Reverso
    resrev = list()
    for i in range(len(revLS)):
        resrev.append(revLS[len(revLS) - i - 1])
    return resrev


def elementor(n1, eleLS):  # Elementor
    resele = False
    for e in eleLS:
        if e == n1:
            resele = True
            return resele
        if (e > n1):
            return resele
    return resele


def maximo(maxLS):  # Máximo
    resmax = maxLS[0]
    for e in maxLS:
        if e > resmax:
            resmax = e
    return resmax


def somaacu(saLS):  # SomaAcu
    ressa = []
    tempsa = 0
    for e in saLS:
        tempsa += e
        ressa.append(tempsa)
    return ressa