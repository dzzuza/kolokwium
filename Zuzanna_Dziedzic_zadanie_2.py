#Zuzanna Dziedzic
h=7
w=11
n=h//2+1

for k in range(n):
  for i in range(h):
    line=''
    for j in range(w):
      if(i<=k-1 or i>=h-k or j<=k-1 or j>=w-k):
        line+='x'
      else:
        line+='0'
    print(line)
  print('\n')
  
for k in range(n+1):
  for i in range(h):
    line=''
    for j in range(w):
      if(i<=k-1 or i>=h-k or j<=k-1 or j>=w-k):
        line+='0'
      else:
        line+='x'
    print(line)
  print('\n')