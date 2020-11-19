mapp = {'97': ' a', '98':' b', '99': ' c', '65': ' A', '66':' B', '67': ' C'}

for k in mapp.keys():
    print(k)

for v in mapp.values():
    print(v)

mapp ['68']= ' D'

for k,v in mapp.items():
    print(k,v)

for k,v in mapp.items():
    if k == '99':
        print(v)

