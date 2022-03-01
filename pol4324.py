file = open('17-4.txt')
file_n = file.read()
A = file_n
k=0
s=0
for i in range (len(A)-1):
  x=i
  if (x%16==11) and (x%7==0) and (x%6!=0) and (x%13!=0) and (x%19!=0):
    k=k+1
    s=s+i
print(s, k)