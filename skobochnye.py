s = str(input("Скобочное выражение: ")).split()
D = {"(": ")", "[": "]", "{": "}"}
S = []

error = False
for i in S:
  if i in D:
    S.append(D[i])
  elif i in D.values():
    if not S or i != S.pop():
      error = True
      break
if S: error = True
if not error: print("Правильно.")
else: print("Неправильно.")


