F = {
}

with open("dictionary.txt") as File:
    while True:
        l = File.readline().rstrip()
        if not l: break
        perevod, slovo = l.split()
        F[slovo] = perevod
print(F)

while True:
    slovo = input("Введите слово для перевода: ")
    if not slovo: break
    if slovo in F:
        print(slovo, '—', F[slovo])
    else:
        print(slovo, "Не знаю.")
        perevod = input("Как переводится это слово? ")
        F[slovo] = perevod
        with open("dictionary.txt", "w") as File2:
            for k, v in F.items():
                File2.write(k + ' ' + v + '\n')