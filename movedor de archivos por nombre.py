#Liberias
from pathlib import Path
import shutil

Route : str
Destination : str
Files : list = []
Choice : str = "3"

#Tipo de accion
while True:
    Choice = input("si quiere mover los archivos presione 1 \nsi quiere copiar los archivos presione 2 \nSi quiere salir de la ejecucion pulse 3 \n :")
    if Choice in ["1", "2", "3"]:
        break
    else:
        print("valor invalido \nIngrese uno nuevo")

#Conseguir rutas
while True:
    option = False
    Route = ""
    Route = input("¿En que ruta carpeta estan los archivos? \n(Si es la misma en la que esta este archivo, solo pulse enter) \n :  ").strip()
    if Route in ["", "."]:
        Route = str(Path(__file__).parent)
    if Path(Route).exists():
        print("La ruta escogida es: " + Route)
        while True:
            match input("Si no esta seguro, presione 1 \nSi esta seguro, presione 2 \n : ").strip():
                case "1":
                    option = False
                    break
                case "2":
                    option = True
                    break
                case _:
                    print("Ingrese un valor valido")
    else:
        print("La ruta es invalida")
    if option:
        break

while True:
    option = False
    Destination = ""
    Destination = input("¿Cual es la ruta a la cual quiere mover los archivos? \n :  ").strip()
    if Path(Destination).exists() and not Destination in ["", "."]:
        print("La ruta escogida es: " + Destination)
        while True:
            match input("Si no esta seguro, presione 1 \nSi esta seguro, presione 2 \n : ").strip():
                case "1":
                    option = False
                    break
                case "2":
                    option = True
                    break
                case _:
                    print("Ingrese un valor valido")
    else:
        print("La ruta es invalida")
    if option:
        break

for i in Path(Route).iterdir():
    Files.append(i)

#Movilizacion de archivos
for i in Files:
    if Path(Destination).exists() or Choice == "3":
        if Choice == "1":
            print(i)
            shutil.move(i, Destination)
        elif Choice == "2":
            print(i)
            shutil.copy(i, Destination)
    else:
        print("El destino no se encuentra disponible se abortara las acciones \nO se escogio salir de la ejecucion")
        break

input("el proceso a terminado preisone enter para cerrar    ")