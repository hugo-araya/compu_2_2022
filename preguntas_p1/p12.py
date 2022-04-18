li = [1, 2, 3, 4]
for i in range(len(li)//2):
	c = li[i]
	li[i] = li[-i-1]
	li[-i-1] = c
print (li)

