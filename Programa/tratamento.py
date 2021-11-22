def entrada(valor, parametro_1, parametro_2):
	if ((valor.isalnum() == True) and (valor.isalpha() == False)):
		if (int(valor) >= parametro_1 and int(valor) <= parametro_2):
			print("Você informol um valor invalido")
			return True


	else:
		return False