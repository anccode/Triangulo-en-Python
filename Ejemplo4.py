#-*- coding : utf-8 -*-

def foreign_exchange_calculator(ammount):
	pass
	mex_to_col_rate = 145.47

	return mex_to_col_rate * ammount

def run():
	pass
	print("Calculadora de divisas")
	print("Convierte pesos mexicanos a pesos colombianos")
	print("")

	ammount = float(input("Ingrese la cantidad de pesos mexicanos que quieres comvertir"))

	foreign_exchange_calculator(ammount)

	result = foreign_exchange_calculator(ammount)
	#format(result,ammount) Define el orden de {},{}
	print("${} pesos mexicanos son ${} pesos colombianos".format(ammount,result))
	print("")

	

if __name__ == "__main__":
	run()