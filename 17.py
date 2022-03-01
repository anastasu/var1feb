file = open('17.txt')
#file_n = file.read()
#A = file_n
k = 0
max_s = 0
s1 = 0
k1 = 0
A = []

while True:
    c = file.readline()
    if c == '':
        break
    A.append(int(c))
for i in range (len(A)-1):
    if A[i] % 2 == 0:
        s1 = s1 + A[i]
        k1 = k1 + 1
    s2 = s1/k1
for i in range (len(A)-1):
    if ((A[i] % 3 == 0) or (A[i+1] % 3 == 0)) and ((A[i] < s2) or (A[i+1] < s2)):
        k = k+1
        max_s = max(max_s, A[i] + A[i+1])
print( max_s, k)