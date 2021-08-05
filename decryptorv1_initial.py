
print('\nInput Ciphertext>')
while True:
    C = str(input())

    LC = len(C)
    uetl = []
    for x in range(LC):
        l = ord(C[x])
        uetl.append(l)
    MM = max(uetl)
    mm = min(uetl)

    if LC%3 != 0:
        print('Ciphertext must be 3n characters long.\n')
        print('Input Ciphertext>')
        continue
    elif mm < 44032 or 55203 < MM:
        print('Includes invalid character.')
        print('\nInput plaintext>')
        continue
    else:
        break

print('\nInput key>')
while True:
    key = str(input())
    
    V = len(key)  
    if 100 < V:
        print('Up to 100 characters allowed for key.\n')
        print('Input key>')
        continue
    elif V < 6:
        print('At least 6 characters required for key.\n')
        print('Input key>')
        continue
    else:
        break

d = 0
for u in range(V):
    b = ord(key[u])
    d = d + b
dd = (59*d)%883

kl00 = []
for t in range(6):
    tv = t + V
    k = ord(key[tv - 6])
    kk = int((k - (k%100))/100)
    f = (tv**5 + tv**4 + 1012*(tv**3) + 18658*(tv**2) + 3429*tv + 393*(k**2) + 5224*k + kk**2 + 174*kk + 3*(dd**2) + 146**dd + 2995)%10000
    sk = str(f).zfill(4)

    kl00.append(sk)

d1 = 0
for u in range(V):
    b = ord(key[u])
    d1 = d1 + b
dd1 = (79*d)%673

kl01 = []
for t in range(6):
    tv = t + V
    k = ord(key[tv - 6])
    kk = int((k - (k%100))/100)
    f = (3*(tv**5) + 8*(tv**4) + 872*(tv**3) + 11846*(tv**2) + 2855*tv + 8239*(k**2) + 5108*k + 667*(kk**2) + 370*kk + 5*(dd1**2) + 342**dd1 + 711)%10000
    sk = str(f).zfill(4)

    kl01.append(sk)

d2 = 0
for u in range(V):
    b = ord(key[u])
    d2 = d2 + b
dd2 = (113*d)%727

kl02 = []
for t in range(6):
    tv = t + V
    k = ord(key[tv - 6])
    kk = int((k - (k%100))/100)
    f = (tv**5 + 4*(tv**4) + 1838*(tv**3) + 15868*(tv**2) + 3411*tv + 771*(k**2) + 8738*k + 11*(kk**2) + 88*kk + 11*(dd2**2) + 194**dd2 + 729)%10000
    sk = str(f).zfill(4)

    kl02.append(sk)

d3 = 0
for u in range(V):
    b = ord(key[u])
    d3 = d3 + b
dd3 = (163*d)%419

kl03 = []
for t in range(6):
    tv = t + V
    k = ord(key[tv - 6])
    kk = int((k - (k%100))/100)
    f = (3*(tv**5) + 2*(tv**4) + 1734*(tv**3) + 14930*(tv**2) + 487*tv + 1115*(k**2) + 3732*k + 83*(kk**2) + 68*kk + 7*(dd3**2) + 658**dd3 + 7299)%10000
    sk = str(f).zfill(4)

    kl03.append(sk)

d4 = 0
for u in range(V):
    b = ord(key[u])
    d4 = d4 + b
dd4 = (97*d)%569

kl04 = []
for t in range(6):
    tv = t + V
    k = ord(key[tv - 6])
    kk = int((k - (k%100))/100)
    f = (2*(tv**5) + 7*(tv**4) + 3589*(tv**3) + 8951*(tv**2) + 248*tv + 1718*(k**2) + 4487*k + 56*(kk**2) + 97*kk + 12*(dd4**2) + 927**dd4 + 4408)%10000
    sk = str(f).zfill(4)

    kl04.append(sk)

k00 = ''.join(kl00).zfill(24)
k01 = ''.join(kl01).zfill(24)
k02 = ''.join(kl02).zfill(24)
k03 = ''.join(kl03).zfill(24)
k04 = ''.join(kl04).zfill(24)

K = [k00, k01, k02, k03, k04]

def D(m):
    return int(str(str(k00[m]) + str(k01[23 - m])))%5

p = [5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
M = [[0,1,2,3],[0,1,3,2],[0,2,1,3],[0,2,3,1],[0,3,1,2],[0,3,2,1],[1,0,2,3],[1,0,3,2],[1,2,0,3],[1,2,3,0],[1,3,0,2],[1,3,2,0],[2,0,1,3],[2,0,3,1],[2,1,0,3],[2,1,3,0],[2,3,0,1],[2,3,1,0],[3,0,1,2],[3,0,2,1],[3,1,0,2],[3,1,2,0],[3,2,0,1],[3,2,1,0]]
Mr = [[0,1,2,3],[0,1,3,2],[0,2,1,3],[0,3,1,2],[0,2,3,1],[0,3,2,1],[1,0,2,3],[1,0,3,2],[2,0,1,3],[3,0,1,2],[2,0,3,1],[3,0,2,1],[1,2,0,3],[1,3,0,2],[2,1,0,3],[3,1,0,2],[2,3,0,1],[3,2,0,1],[1,2,3,0],[1,3,2,0],[2,1,3,0],[3,1,2,0],[2,3,1,0],[3,2,1,0]]

klkl = []
for n in range(24):

    kn = []
    for t in range(p[n]):
        tk = t + int(K[D(0)][n])
        k = ord(key[(p[n] - t - 1)%V])
        kk = int((k - (k%100))/100)
        f = (tk**5 + tk**4 + (971 + int(K[D(1)][n]))*(tk**3) + (16947 - int(K[D(2)][n]))*(tk**2) + (2279+int(K[D(3)][n]))*tk + (282 - int(K[D(4)][n]))*(k**2) + (4103+int(K[D(5)][n]))*k + kk**2 + (194-int(K[D(6)][n]))*kk + 3411*n + 841*t*n + 7407*t + 5988)%10000
        sk = str(f).zfill(4)
        kln = sk[M[(11*n + n*t + 7*t + 5*int(K[D(7)][n]))%24][int(K[D(8)][n])%4]]
        kn.append(kln)
        knl = ''.join(kn)
        
    klkl.append(knl)

lxx = []
for i in range(int(LC/3)):
    for j in range(24):
        lxx.append(str((int(K[D(9)][j])*p[1 + (i%23)] + 22*(i**2) + 13*i + 17*j)%10))

G = 8*LC
for i in range(G):
    for u in range(4):
        lxx[i] = str((int(lxx[i]) + int(lxx[(i + p[20 + u])%int(4*LC/12)]))%10)
    lxx[i] = lxx[(i - (int(K[D(10)])%24))%G]

X = (int(K[D(11)][8] + K[D(12)][19]) + 5*i)%16
W = str(bin(X)[2:].zfill(4))

cq =[]
for i in range(int(LC)):
    cq.append((int(str(lxx[4*i + int(W[0])]) + str(lxx[4*i + int(W[1]) + 1]) + str(lxx[4*i + int(W[2]) + 2]) + str(lxx[4*i + int(W[3]) + 3])) + int(K[D(13)])%((27*i + 7)%(p[i%24]*p[(i+11)%24]) + 3))%24)

Rb = []
for i in range(LC):
    
    o = ord(C[i])
    g = int(K[D((2*i)%24)] + K[D((2*i + 1)%24)])%11172
    
    if g < 10000:
        if o - g < 44032:
            irsb = str(o - 44032).zfill(4)
        else:
            irsb = str(o - 45204).zfill(4)
    else:
        if (o - g)%2 == 0:
            irsb = str(int((o - g - 34032)/2)).zfill(4)
        else:
            irsb = str(int((o - g - 24031)/2)).zfill(4)

    m = []
    for w in range(4):
        m.append(irsb[Mr[cq[i]][w]])
    
    irs = ''.join(m)
    Rb.append(irs)

Rc = ''.join(Rb)
Rrb = Rc.replace('-', '0')
R = list(Rrb)
LR = len(R)

for h in range(24):
    i = 23 - h

    e = i%6
    if e < 3:
        for j in range(LR):
            R[(17*i + j)%LR] = str((int(R[(17*i + j)%LR]) - (e - 3)*int(klkl[i][j%p[i]]))%10)
    else:
        for j in range(LR):
            R[(17*i - j)%LR] = str((int(R[(17*i - j)%LR]) - (e - 2)*int(klkl[i][j%p[i]]))%10)

Ro = R
for h in range(7):
    j = 6 - h

    for b in range(LR):
        i = LR - 1 - b
        Ro[i] = str((int(R[i]) - int(R[(i + j - p[23 - j] + 1)%LR]))%10)
        R[i] = str((int(Ro[i]) - int(Ro[(i - j - 1)%LR]))%10)

Rx = []
for i in range(LR):
    Rx.append(R[(i - int(klkl[0]))%LR])

t = []
for x in range(int(LR/6)):
    
    Y = []
    for j in range(6):
        Y.append(Rx[6*x + j])
    y = int(''.join(Y))

    for u in range(V):
        k = ord(key[u])
        stringkb = str(bin(u**3 + u)[2:].zfill(47))
        stringko = str(oct(u**3 + u)[2:].zfill(17))
    
    z = int((902708 - 15394*((8*x)%11) - 9705*(6 - ((5*(x**2))%7)) - 7817*(12 - ((4*x)%13)) - 4211*(((3*(k**2)) + 5*x)%16) + 2981*(((ord(key[x%V]))%100)%5) - 2692*(22 - ((6*(x**2))%23)) + 179*((2*(k**3))%37) - 41*(886 - (x%887)) + 17*(((x**4) - 19*(x**3) + 270*x)%643) + 129*(int(stringkb[(6*x)%47])) + 301*(int(stringko[16 - ((2*x)%17)] + 2) - y))/(int(stringkb[46 - (x%47)]) + 1))
    
    t.append(chr(z))

if len(t) != int(2*LC/3):
    print('Error')
    exit()

if '𱍊' in t:
        t.remove('𱍊')

P = ''.join(t)
print('\nPlaintext:\n')
print(P, '\n')
print('Ciphertext length =', LC)
print('Key length =', V)
print('Plaintext length =', int(LR/6), '\n')