# File Mover by Name / Movedor de archivos por nombre

![Version](https://img.shields.io/badge/version-1.1-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.10%2B-yellow)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20Mac-lightgrey)

## Table of content / Tabla de contenido

- [English](#english)
    - [Description](#description)
    - [Features](#features)
    - [How to run it?](#how-to-run-it)
    - [How does the program work?](#how-does-the-program-work)
    - [Requirements](#requirements)
    - [Recommendations](#recommendations)
    - [Limitations](#limitations)
    - [License](#license)
    - [Contributions](#contributions)
    - [Version](#version)

- [Español](#español)
    - [Descripcion](#descripcion)
    - [Caracteristicas](#caracteristicas)
    - [¿Como ejecutarlo?](#como-ejecutarlo)
    - [¿Como funciona el programa?](#como-funciona-el-programa)
    - [Requisitos](#requisitos)
    - [Recomendaciones](#recomendaciones)
    - [Limitaciones](#limitaciones)
    - [Licencia](#licencia)
    - [Contribuciones](#contribuciones)
    - [Versión](#versión)

## English

> Note: English is not my first language, so there may be minor translations errors

### Description

This Python script is designed to move or copy files in alphabetical order, whether on the same device or on an external device.
You don’t need to pass the data through the terminal, as it doesn’t support that; instead, it requests the information bit by bit—specifically, the location, range, and modification type.
This project originated from an issue with generic MP3 players, where songs usually play out of order. However, I discovered that the order is determined by the order in which they are stored in memory.
The program will move or copy files in alphabetical order, so a numerical code at the beginning can be used to move or copy them in a custom order.
If you have a large number of files, I have a program that can help with inserting or deleting files while maintaining a clean order, called [Code Renamer](https://github.com/DeveloperMii/Code-Renamer...Renombrador-de-codigo) it basically adds or subtracts positions from each file’s index to keep things more organized.

### Features

- Sorts files alphabetically
- Supports any system path (provided the program has the appropriate permissions)
- Compatibility with external devices
- Protection against device removal (Aborts actions in this case)

### How to run it?

#### Python File Option (.py)

1. Download the program from the release section.
2. Install Python 3.10 or higher.
3. You can run the file from the terminal or by double-clicking it.
4. Enter the requested information and press Enter to continue.

#### Windows Executable (.exe) Option

1. Download the program from the release section.
2. You can run the file from the terminal or by double-clicking it.
3. Enter the requested information and press Enter to continue.

### How does the program work?

The program runs in the terminal and prompts the user for input step by step:

1. Asks the user to select an action: Copy / Paste / Exit (for added security)
2. Asks for the path where the files are located
3. Asks for the destination path for the files
4. Stores the path to each file in an array
5. Uses a for loop to process each file one by one

### Requirements

#### Python File Option (.py)

- Python 3.10 or higher
- pip
- Operating System
    - Windows 10 or higher / Linux (compatible with Python 3.10 or higher) / Mac (compatible with Python 3.10 or higher)

#### Windows Executable (.exe) Option

- Windows 10 or 11

### Recommendations

- If you want a sorting order other than alphabetical, you can add a numeric code at the beginning of each file name, as numbers take precedence over letters
- The recommended use of this program is to play songs in a specific order on an MP3 player
- Do not disconnect the device to which you are moving files; if this happens, the process will be canceled

### Limitations

- The program will move/copy everything in that folder; therefore, if the folder is very large, errors may occur if there is insufficient storage space
- If you are using a numeric code and have a large number of files, I recommend using [Code Renamer](https://github.com/DeveloperMii/Code-Renamer...Renombrador-de-codigo) to streamline the management of the numeric code when adding, removing, or inserting files

### License

This project is licensed under the MIT License.

### Contributions

Pull Requests are not currently accepted.
If you find a bug or wish to suggest an improvement, open an issue explaining the issue.
The project may be freely modified via a fork, but such versions will not be associated with the official version

### Version

Current version: 1.1

## Español

> Esta es la versión original del README

### Descripcion

Este Script de Python tiene la funcion de mover/copiar archivos de manera alfabetica sea en el mismo dispositivo o en un dispositivo externo.
No es necesario pasarle los datos por la terminal, ya que no los soporta el los va pidiendo poco a poco en total son ubicación, rango, y tipo de modificación.
Este proyecto nacio con una complicacion en reproductores mp3 genericos que generalmente las canciones salen en desorden pero descubri que el orden viene dictaminado por el orden en el que entran a la memoria.
El programa movera o copiara en orden alfabetico por lo que un codigo numerico al inicio puede usarse para mover o copiar en un orden propio.
En caso de tener muchos archivos tengo un programa que puede ayudar a la insercion o eliminacion de archivos y mantener el orden limpio llamado [Renombrador de codigo](https://github.com/DeveloperMii/Code-Renamer...Renombrador-de-codigo) basicamente añade o sustrae posiciones a cada indice de los archivos manteniendo mas ordenado

### Caracteristicas

- Mueve archivos de manera alfabetica
- Cualquier ruta del sistema es compatible (Siempre y cuando el programa cuente con los permisos adecuados)
- Compatibilidad con dispositivos externos
- Proteccion contra remocion del dispositivo (Aborta las acciones en este caso)

### ¿Como ejecutarlo?

#### Opcion Archivo de Python (.py)

1. Descargar el programa desde el apartado de release.
2. Instalar Python 3.10 o superior.
3. Puedes ejecutar el archivo desde la terminal o dándole doble clic.
4. Escribir los datos que pida y pulsar enter para continuar.

#### Opcion Ejecutable de Windows (.exe)

1. Descargar el programa desde el apartado de release.
2. Puedes ejecutar el archivo desde la terminal o dándole doble clic.
3. Escribir los datos que pida y pulsar enter para continuar.

### ¿Como funciona el programa?

El programa se ejecuta en terminal y pide datos poco a poco:

1. Pide al usuario la accion a realizar Copiar / Pegar / Salir (para mas seguridad)
2. Pide la ruta donde estan los archivos
3. Pide la ruta hacia donde van los archivos
4. Mete la ruta a cada archivo en un array
5. Mediante un bucle for mueve uno a uno cada archivo

### Requisitos

#### Opcion Archivo de Python (.py)

- Python 3.10 o superior
- pip
- Sistema operativo
    - Windows 10 o superior / Linux (compatible con Python 3.10 o superior) / Mac (compatible con Python 3.10 o superior)

#### Opcion Ejecutable de Windows (.exe)

- Windows 10 o 11

### Recomendaciones

- En caso de querer un orden distinto al alfabetico al inicio del nombre de cada archivo puede añadir un codigo numerico ya que los numeros tienen prioridad sobre las letras
- El uso recomendado de este programa es para que las canciones se reproduzcan en cierto orden en un reproductor mp3
- No desconecte el dispositivo al que esta moviendo archivos en caso dado que eso suceda la ejecucion se cancelara

### Limitaciones

- El programa va a Mover/Copiar todo lo que este en dicha carpeta por ende si el tamaño es muy grande pueden surgir errores en caso de que el almacenamiento no sea suficiente
- En caso de tener codigo numerico y mucha cantidad de archivos recomiendo usar [Renombrador de codigo](https://github.com/DeveloperMii/Code-Renamer...Renombrador-de-codigo) para agilizar el control del codigo numerico en caso de adicion, Sustracion o Insercion de archivos

### Licencia

Este proyecto está bajo licencia MIT.

### Contribuciones

Actualmente, no se aceptan Pull Requests.
Si encuentras un error o deseas sugerir una mejora, abre un issue explicando el caso.
El proyecto puede ser modificado libremente mediante un fork, pero dichas versiones no estarán asociadas a la versión oficial

### Versión

Versión actual: 1.1