a = True
b = '1'
c = 2
while b[-1] not in '378':
    if len(b)%2 == 0:
        a = True
    if a == True:
        c = c * 7
    b = b + str(c)
print (c)

