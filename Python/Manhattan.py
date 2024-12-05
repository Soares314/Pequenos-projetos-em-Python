def caminho(nos):
  contador = 0
  i = 0
  j = 0
  while i < len(nos):
    while i<4:
      contador = contador + nos[i]
      i = i + 1
      if(j == 24):
        break
  return contador

tes = 10
pes = 2**tes
mase = [[0] * tes for _ in range(pes)]
mase[0][0] = 0
mase[1][0] = 1
i = 0
j = 0
while(i != tes-1):
  x = 0
  i = i + 1
  j = 2**i
  while(x < j):
    y = 0
    while(y < i):
      mase[x+j][y] = mase[x][y]
      y = y + 1
    mase[x+j][y] = 1
    x = x + 1

print(mase)