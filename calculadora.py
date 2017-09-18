while True:
	print("Opciones:")
	print("1)para sumar esciba la palabra 'suma'")
	print("2)para restar escriba la palabra 'resta'")
	print("3)para multiplicar escriba la palabra 'multiplicar'")
	print("4)para dividir escriba la palabra 'dividir'")
	print("5)para salir escriba la palabra 'salir'")

	user_input = input(":")

	if user_input == "salir":
		
		print("gracias por usar este programa :) ")	
		break
	
	elif user_input == "suma":
		num1 = float(input("Ingresa un número: "))
		num2 = float(input("Ingrese otro número: "))

		resultado=str(num1 + num2)
		
		print ("|El resultado es: " + resultado)
		print("")
		
	elif user_input == "resta":
		num1 = float(input("Ingresa un número: "))
		num2 = float(input("Ingrese otro número: "))

		resultado = str(num1 - num2)

		print("|El resultado es: " + resultado)
		print("")

	elif user_input == "multiplicar":
		num1 = float(input("Ingresa un número: "))
		num2 = float(input("Ingrese otro número: "))

		resultado = str(num1 * num2)

		print ("|El resultado es: " + resultado)
		print("")

	elif user_input == "dividir":
		num1 = float(input("Ingresa un número: "))
		num2 = float(input("Ingrese otro número: "))

		resultado = str(num1 / num2)

		print ("|El resultado es:  " + resultado)
		print("")

	else:
		print("sentencia invalida")
		print("")