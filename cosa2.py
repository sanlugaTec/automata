def Numeros(n):
	estado = "q1"
	for num in n:
		Delta = (estado,num)
		if Delta ==  ("q1","0") or Delta == ("q2","0"):
			estado = "q1"
			print estado
		elif Delta ==  ("q1","1") or Delta == ("q2","1"):
			estado = "q2"
			print estado
	if estado == "q2":
		print "acpetable"
	else:
		print "no aceptable"

Numeros("1001010")