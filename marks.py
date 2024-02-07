class pupil:
    firstname = ''
    surname = ''
    algebra = ''
    russian = 0
    fizika = 0
    history = 0

Pupils = []
File = open("marks.csv")

for line in File:
    a = pupil()
    data = line.rstrip().split(',')
    a.firstname = data[0]
    a.surname = data[1]
    a.algebra = int(data[2])
    a.russian = int(data[3])
    a.fizika = int(data[4])
    a.history = int(data[5])
    Pupils.append(a)
File.close()

N = len(Pupils)
sumAlgebra = sumRussian = sumFizika = sumHistory = 0
for a in Pupils:
  sumAlgebra += a.algebra
  sumRussian += a.russian
  sumFizika += a.fizika
  sumHistory += a.history

print("Средние баллы: ")
print("Алгебра: ", sumAlgebra/N)
print("Русский язык: ", sumRussian/N)
print("Физика: ", sumFizika/N)
print("История: ", sumHistory/N)

maxball = 0
for a in Pupils:
  s = a.algebra + a.russian + a.fizika + a.history
  maxball = max(maxball, s)

print("Максимальный балл:", maxball)

Pupils.sort(key = lambda x: x.firstname)
for a in Pupils:
  s = a.algebra + a.russian + a.fizika + a.history
  if s == maxball:
    print(a.firstname, a.surname)

a2 = 0
for a in Pupils:
  if 2 in [a.algebra, a.russian, a.fizika, a.history]:
    a2 += 1

print("Получили 2:", a2, "человек")