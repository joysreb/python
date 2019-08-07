tuplex=('p','y','t','t','h','o','n')
print(tuplex)
tuplex=tuplex[:2]+tuplex[2:]
print (tuplex)
listx=list(tuplex)
listx.remove('t')
tuplex=tuple(listx)
print (tuplex)
