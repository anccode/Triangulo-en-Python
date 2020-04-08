#-*- coding : utf-8 -*-
def convreter(selection,currency):
	
	dolar = 3.46
	sol = 1
	pass
	if selection == 1:
		pass
		return (currency * sol)/
	elif selection == 2:
		pass
		return currency / dolar 
def main():
	pass
	print("Convertidor de moneda (Sol Peruano y dolares)")
	selection = int(input("Selecione 1:Dolar a Sol Peruano 2:Sol Peruano a Dolar"))

	if selection == 1:
		pass
		currency = int(input("Seleccione el valor de la moneda"))
	elif selection == 2 :
		pass
		currency = int(input("Seleccione el valor de la moneda"))
	else:
		return print("No selecciono valores validos")

	converter(selection, currency)

	result = converter(selection, currency)
	
	print("El resultado es ${}".format(result))


if __name__ == "__main__":
	main()