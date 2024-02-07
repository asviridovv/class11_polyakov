F = {
}

with open("slova.txt", encoding="utf8") as File:
    while True:
        word = File.readline().strip()
        if not word: break
        F[word] = F.get(word, 0) + 1
    File.close()
with open("slovaout.txt", "w") as File:
    for k in sorted(F):
        File.write(k + ": " + str(F[k]) + "\n")

for i in F.values():
    print(i)