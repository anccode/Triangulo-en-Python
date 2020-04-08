#-*- coding : utf-8 -*-
#Ejemplo de un triangulo Equilatero
import turtle

def main():
	
	#En Python3 no es necesario poner window
	#window = turtle.Screeen()
	side = turtle.Turtle()
	make_triangle(side)
	turtle.mainloop()

def make_triangle(side):
	pass
	length = int(input("Ingrese el Tamaño del Tiangulo Equilatero: "))

	for i in range(3):
		pass
		make_line_and_turn(side, length)

def make_line_and_turn(side, length):
	pass
	side.forward(length)
	side.left(240)

if __name__ == '__main__':
	main()

