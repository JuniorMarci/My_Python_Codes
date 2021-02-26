arr = [1,2,3,8,3,8,8,4,6,1,1,1,1,4,4,4,12]
qnt = 6


ordem = sorted (arr, reverse=True)
resultado = []
c = 0

for n in range (len (ordem)):
  if c > (qnt-1):
    pass
  else:
    if ordem[n]==ordem[n+1]:
      resultado.append (ordem[n])
    else:
      c = c+1
      resultado.append (ordem[n])


print (ordem)
print (resultado)
