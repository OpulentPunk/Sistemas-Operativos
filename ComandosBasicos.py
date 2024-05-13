import subprocess

def ejecutar (comando):
    subprocess.run(comando,shell=True)

while True:
    print("1. Crear un archivo txt llamado 'misnotas.txt'")
    print("2. Crear una carpeta que se llame 'Calificaciones'")
    print("3. Crear una carperta dentro de 'Calificaciones' que se llame 'Primer Parcial'")
    print("4. Mover el archivo 'misnotas.txt' a la carpeta de 'Calificaiones'")
    print("5. Dentro de la carpeta Primer Parcial se moverá 'Calculadora.py'")
    print("6. Salir del programa")

    opc=str(input("¿Que desea realizar?: "))

    if opc=="1":
        ejecutar("touch misnotas.txt")
    elif opc=="2":
        ejecutar("mkdir Calificaciones")
    elif opc=="3":
        ejecutar("mkdir Calificaciones/Primer_Parcial")
    elif opc=="4":
        ejecutar("mv misnotas.txt Calificaciones")
    elif opc=="5":
        ejecutar("mv Calculadora.py Calificaciones/Primer_Parcial")
    elif opc=="6":
        print("Saliendo...")
        break
    else:
        print("Ponga una opción válida")



        


