F = input().split()

stack = []
for a in reversed(F):
    if a in "+-*/":
        oper = int(stack.pop())
        oper1 = int(stack.pop())
        if a == "+": b = oper + oper1
        elif a == "-": b = oper - oper1
        elif a == "*": b = oper * oper1
        else: b = oper // oper1
        stack.append(b)
    else:
        stack.append(a)
    print(stack)
print("Результат:", stack[0])
