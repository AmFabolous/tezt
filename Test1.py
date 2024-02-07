from math import pi, sin

def f(x):
    return sin(x)

a = pi/2
b = 7*pi/6
n = 10000000
dx = (b - a) / n
sumV = 0
sumH = 0

for i in range(n):
    sumV += f(a + i*dx)*dx
    sumH += f(a + (i+1)*dx)*dx

rsum = (sumV + sumH) / 2
print(f'En tilnærmet verdi for roten av 3 delt på 2 blir {rsum}')
