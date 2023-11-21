def make(a):
    if a>0:
        return a * -1
    elif a == 0:
        return 0
    else:
        return a

# saf =  int (input('введите число:'))        
# make(saf)
def between(s, d):
    return list(range(s, d + 1))
# dasc = between(1,8)
# print(dasc)

def is_d(x,y,z):
    if x % y ==0 and x % z == 0:
        return True
    else:
        return False
# print(is_d(4,26,1))

def find_average(q):
    e = 0
    for w in q:
        e += w
    return e / len(q) 
# print(find_average([]))

def rueyu(q,w):
   return q * w
# print(rueyu(0,"rery"))

# print (min(5,67,3))

def re(r):
    if r == True:
        return "yes"
    else:
        return "no" 
# print(re(True))

def ty(r,t):
    return sum(r) + sum (t) #sum(r + t)
# print(ty([3,3,2],[332233,33323]))

def fus(q):
    if q == 0:
        return ''
    elif q == 1:
        return "+"
    elif q == 2:
        return '++\n++'
    else:
        return "+" * q + "\n" + '+'*q +  (q - 2)*('\n' + '+'*q)

print(fus(1))