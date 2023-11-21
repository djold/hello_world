
with open("lir.txt","r") as f:
    q = f.read()
    
w = ''
e = []
for i in q.lower():
    
    if i in " ,.-_!?<>'\"\n«»—":
        if w == "":
            pass
        else :
            e.append(w)
            w = ""
    else:
        w += i

print(e)
dict_count = {}
for m in e:
    if m not in dict_count:
        dict_count[m] = 1
    else:
        dict_count[m] += 1

print(dict_count)

