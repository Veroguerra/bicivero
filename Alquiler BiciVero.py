import random
import sqlite3


# Función para generar un número de tarjeta aleatorio
def generar_numero_tarjeta():
    return random.randint(1000, 9999)

# Función para registrar un usuario
def registrar_usuario():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    correo = input("Ingrese su correo: ")
    tarjeta = generar_numero_tarjeta()
    
    conn = sqlite3.connect('prestamos_bicicletas.db')
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO usuarios (tarjeta, nombre, apellido, correo) VALUES (?, ?, ?, ?)', (tarjeta, nombre, apellido, correo))
    
    conn.commit()
    conn.close()
    
    print(f"Su número de tarjeta es: {tarjeta}")
    return tarjeta

# Función para iniciar sesión
def iniciar_sesion():
    tarjeta = int(input("Ingrese su número de tarjeta: "))
    conn = sqlite3.connect('prestamos_bicicletas.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM usuarios WHERE tarjeta = ?', (tarjeta,))
    usuario = cursor.fetchone()
    
    conn.close()
    
    if usuario:
        print(f"Bienvenido, {usuario[1]} {usuario[2]}")
        return tarjeta
    else:
        print("Número de tarjeta no válido. Intente nuevamente.")
        return None

# Función para registrar el préstamo de una bicicleta
def registrar_prestamo(tarjeta, origen, destino):
    # Aquí puedes implementar la lógica para asignar un número de bicicleta
    # Puedes usar una lista para llevar un registro de las bicicletas disponibles
    bicicletas_disponibles = [1, 2, 3, 4, 5]  # Ejemplo de bicicletas disponibles

    # Verificamos si hay bicicletas disponibles
    if bicicletas_disponibles:
        bicicleta_asignada = bicicletas_disponibles.pop()  # Asignamos una bicicleta disponible
        print(f"Se le ha asignado la bicicleta número {bicicleta_asignada}.")
    else:
        print("Lo sentimos, no hay bicicletas disponibles en este momento.")

# Crear la tabla de usuarios si no existe
conn = sqlite3.connect('prestamos_bicicletas.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        tarjeta INTEGER PRIMARY KEY,
        nombre TEXT,
        apellido TEXT,
        correo TEXT
    )
''')

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

# Ciclo principal
while True:
    print("\n1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        tarjeta = registrar_usuario()
    elif opcion == '2':
        tarjeta = iniciar_sesion()
        if tarjeta:
            origen = input("Ingrese el origen: ")
            destino = input("Ingrese el destino: ")
            registrar_prestamo(tarjeta, origen, destino)
    elif opcion == '3':
        break
    else:
        print("Opción no válida. Intente nuevamente.")
