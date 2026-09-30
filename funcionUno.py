import datetime

def saludar():
    print("Hola,Bienvenid@s")

saludar()

def mostrar_hora():
    hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"La hora actual es: {hora_actual}")

mostrar_hora()

def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

resultado = calcular_area_triangulo(10, 5)
print(f"El área del triángulo es: {resultado}")

def saludar_persona(nombre, edad):
    print(f"Hola {nombre}, tienes {edad} años")
saludar_persona("Esaul",17)


def mostrar_mensaje():
    print("practica en python")

mostrar_mensaje()

def mostrar_operacion():
    print(10 * 5)

mostrar_operacion()


def doble(numero):
    return numero * 10

resultado = doble(5)

print(resultado)