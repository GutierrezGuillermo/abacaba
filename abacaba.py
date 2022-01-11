#El desafío consiste en imprimir las 26 iteraciones de abacaba
#sin imprimir las 26 iteraciones, sólo la ultima siguiendo estas reglas:
#la primera iteración es A, la segunda es B y añade A (aba), la tercera
# añade c, por lo que sería abacaba, y así...

def abacaba(n):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    if n < 1:
        return ""
    else:
        s = abacaba(n-1)
        return s + alfabeto[n-1] + s

prueba = abacaba(1)
print(prueba)
