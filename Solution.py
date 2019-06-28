t = int(input())
while t:
  n, d = input().split(" ")
  a = list(n)
  m = min(a)
  z = [i for i, j in enumerate(a) if j == m]
  l = len(z)
  k = len(a)
  c=""
  for x in z:
    c = c + a[x]
  for i in range(z[-1], k+z[-1]):
    if i in z:
      pass
    else:
      if i < k:
        if a[i] < d:
          c = c + a[i]
        else:
          c = c + d
      else :
        c = c + d
  g = list(c)
  g.sort()
  e=""
  for i in g:
      e+=i
  print(int(c))
  t-=1
