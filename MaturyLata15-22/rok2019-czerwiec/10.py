F = open("liczby.txt")

Dane = []

for line in F:
    Dane.append(line.rstrip())

def CzyPierwsza(x):
    for i in range(2,round(x**(1/2))+1):
        if x % i == 0:
            return False
    return True

for liczba in Dane:
    if CzyPierwsza(int(liczba)):
        if int(liczba)>= 100 and int(liczba) <= 5000:
            print(liczba)

