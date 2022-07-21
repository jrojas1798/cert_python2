#Laboratorio 2.8.1.4
def read_int(prompt, min, max):
    ok= False
    while not ok:
        try:
            value = int(input(prompt))
            ok = True
        except ValueError:
            print("Error: Entrada Incorrecta")
        if ok:
            ok = value >= min and value <= max
        if not ok:
            print("Error: El valor no esta permitido dentro del rango("+str(min) + "<-->"+str(max) + ")")
    return value;

v = read_int("Ingresa un numero entre -10 a 10: ", -10, 10)

print("El número es:", v)
