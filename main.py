from fractions import Fraction

def exo1_1x2():
    
    return f'{10*10} {10+10} {10-1} {10**3} {100//3} {100/3} {100%3}\n{10.*10} {10.+10} {10.-1} {10.**3} {100.//3} {100./3} {100.%3}'

def exo2_1():
    return 0.000001 == 1e-6, 1000 == 1e3, 0.0134 == 1.34e-2

def exo3_2():
    return (10e10 + 10e-10)/10e10 == 1

def exo3_3():
    return 1e5-1e-5,1e7-1e-7,1e9-1e-9,1e10-1e-10,

def exo3_4():
    a = Fraction(1, 2)
    print(a)
    b = Fraction(1, 3)
    print(b)
    print(a + b)

def exo3_6():
    X = 10 ** 10
    Y = Fraction(X + Fraction(1, X), X)
    return X, Y




print(exo3_5())
