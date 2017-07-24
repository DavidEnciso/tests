a='12345'

def flip(s, p1, p2):
    #print('b:',s)
    sd = dict(zip(list(range(len(s))), s))
    #print('dict:', sd)
    i1 = s[p1]
    i2 = s[p2]
    sd[p2] = i1
    sd[p1] = i2
    ret = ''.join(sd.values())
    #print('a:',ret)
    return ret
    
def nx(r):
   #flip first
   o = r
   l = len(r)-1
   print("back")
   m, st = scan(r, o, l, di=-1)
   #print(m, st)
   #if st:
       #return m
   print("fwd")
   n, st = scan(m, o, l, di=1)
   #print(n, st)
   if st:
       return n
   return o

def scan(r, o, l, di=1):
    bgn, end = (l, 0) if di == -1 else (0, l)
    #print(list(range(bgn, end, di)))
    prv = o
    for j in list(range(l)):
        for i in list(range(bgn, end, di)):
            #print(i)
            #print(i, i+di)
            if di == 1:
                sd = flip(r, i, l)
            else:
                sd = flip(r, i, l)
            #print(sd)
            if int(sd) > int(prv):
                #return sd, True
                prv = sd
                print(sd)
            r = sd
    return r, False

print(a)
#print(flip(a, len(a)-1, len(a)-2))
print(nx(a))

