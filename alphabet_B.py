F = {
}

with open("slova.txt", encoding="utf8") as File:
    while True:
        word = File.readline().strip()
        if not word: break
        F[word] = F.get(word, 0) + 1
    File.close()

w1 = [(w,F[w]) for w in F]
w1.sort(key = lambda x: (-x[1], x[0]))

with open("slovaout.txt", "w") as File:
    for word, count in w1:
        File.write(word + ": " + str(count) + "\n")

for i in F.values():
    print(i)