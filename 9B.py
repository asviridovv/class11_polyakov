from math import pi

r = 0.0033
m = 0.15
v = 20
delt = 0.001
C = 0.4
ro = 1.23
S = pi*r*r
g = 10
t = 0
y = 0
h = 0
t1 = 2*v/g
h1 = v*v/2/g
v1 = -v

while y >= 0:
    f = -ro*abs(v)*v*C*(S/2)
    a = -g + f/m
    y = y + v*delt + a*delt*(delt/2)
    v = v + a*delt
    t = t + delt
    if y > h:
        h = y

print(f"Без учёта сопротивления t = {t1}, h = {h1}, v = {v1}")
print(f"С учётом сопротивления t = {t}, h = {h}, v = {v}")
