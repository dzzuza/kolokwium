lista=input("podaj listę liczb: ")

tab=[]
number=''
for x in lista:
  if(x!=' '):
    number+=x
  else:
    tab.append(number)
    number=''
tab.append(number)

print('lista po usunięciu liczb, których suma dzielników właściwych jest nieparzysta:')
for i in tab:
  suma=0
  if(i!=' '):
    for div in range(1,int(i)//2+1):
      if(int(i)%div==0):
        suma=suma+div
  if(suma%2==1):
    print(i)