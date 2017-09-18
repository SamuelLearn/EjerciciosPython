# funciones matemátcas

def suma (num1 , num2):
	resultado = str(num1 + num2)
	print("");print("La suma es: " + resultado);print("")

def resta (num1 , num2):
	resultado = str(num1 - num2)
	print("");print("La resta es: " + resultado);print("")

def multi (num1 , num2):
	resultado = str(num1 * num2)
	print("");print("La multiplicación es: " + resultado);print("")

def divi (num1 , num2):
	resultado = str(num1 / num2)
	print("");print("La división es: " + resultado);print("")

def menu():
	print("...:::Opciones:::...")
	print("1)para sumar esciba la palabra 'suma'")
	print("2)para restar escriba la palabra 'resta'")
	print("3)para multiplicar escriba la palabra 'multiplicar'")
	print("4)para dividir escriba la palabra 'dividir'")
	print("5)para salir escriba la palabra 'salir'")


#calculadora

while True:
	menu()

	user_input=input(":")

	if user_input == "salir":
		print ("Gracias por usar este programa :3")
		break
	elif user_input == "suma":

		num1 = float(input("Ingrese un número: "))
		num2 = float(input("Ingrese un número: "))
		
		suma(num1 , num2)

	elif user_input == "resta":
		
		num1 = float(input("Ingrese un número: "))
		num2 = float(input("Ingrese un número: "))
		
		resta(num1 , num2)

	elif user_input == "multiplicar":

		num1 = float(input("Ingrese un número: "))
		num2 = float(input("Ingrese un número: "))
		
		multi(num1 , num2)

	elif user_input == "dividir":

		num1 = float(input("Ingrese un número: "))
		num2 = float(input("Ingrese un número: "))
		
		divi(num1 , num2)
	else:
		print("");print("Error no existe ese comando");print("")