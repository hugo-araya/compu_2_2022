linea = "AAGADGA"
suma = 0
for i in range(len(linea)):
	for j in range(i+1, len(linea)):
		if linea[i] > linea[j]:
			suma = suma + 1
print (suma)
