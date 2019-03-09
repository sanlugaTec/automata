def Automata(n):
	delta = [[0, 1], [0, 1]]
	actual = 0
	qF = 1

	for num in n:
		print delta
	 	actual = delta[actual][int(num)]

	if actual==qF:
		print "aceptado"
	else:
		print "no aceptado"

Automata("1001011111111")