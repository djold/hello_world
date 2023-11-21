def appiy_to_each(L,F):
    for i in range(len(L)):
        L[i] = F(L[i])
    L += 'tyhj'
    return L
x = [1,-7,32,6.3, 9.1]
def change(q):
    return q * -1
print(appiy_to_each(x,change))
print(x)