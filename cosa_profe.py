
def Numeros(n):
	estado = "q1"
	for number in n:
		if estado == "q1"  and number == "0":			
			estado = "q1"
			print estado
		elif estado == "q2" and number == "0":
			estado = "q1"
			print estado
		elif estado == "q2" and number == "1":
			estado = "q2"
			print estado
		elif estado == "q1" and number == "1":
			estado = "q2"
			print estado
		else:
			print "no existe el numero "

	if estado == "q2":
		print "acpetable"
	else:
		print "no aceptable"


Numeros("011101000")