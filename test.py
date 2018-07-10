d = {'a':1, 'b':2}
plain = ['a', 'b']
rev = ['b', 'a']

c = {}
for i, k in enumerate(plain):
    c[rev[i]] = d[k]

print(c)
