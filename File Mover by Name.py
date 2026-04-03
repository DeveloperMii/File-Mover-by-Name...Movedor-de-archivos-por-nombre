#Libraries
from pathlib import Path
import shutil

#Variables
Route : str
Destination : str
Files : list = []
Choice : str = "3"

#Type of action
while True:
    Choice = input("If you want to move the files, press 1 \nIf you want to copy the files, press 2 \nIf you want to exit, press 3 \n :")
    if Choice in ["1", "2", "3"]:
        break
    else:
        print("Invalid value \nPlease enter a new one")

#Get routes
while True:
    option = False
    Route = ""
    Route = input("In which folder are the files located? \n(If it's the same folder as this file, just press Enter) \n :  ").strip()
    if Route in ["", "."]:
        Route = str(Path(__file__).parent)
    if Path(Route).exists():
        print("The chosen route is: " + Route)
        while True:
            match input("If you're not sure, press 1 \nIf you're sure, press 2 \n : ").strip():
                case "1":
                    option = False
                    break
                case "2":
                    option = True
                    break
                case _:
                    print("Enter a valid value")
    else:
        print("The path is invalid")
    if option:
        break

while True:
    option = False
    Destination = ""
    Destination = input("What is the destination path for the files? \n :  ").strip()
    if Path(Destination).exists() and not Destination in ["", "."]:
        print("The chosen route is: " + Destination)
        while True:
            match input("If you're not sure, press 1 \nIf you're sure, press 2 \n : ").strip():
                case "1":
                    option = False
                    break
                case "2":
                    option = True
                    break
                case _:
                    print("Enter a valid value")
    else:
        print("The path is invalid")
    if option:
        break

for i in Path(Route).iterdir():
    Files.append(i)

#File migration
for i in Files:
    if Path(Destination).exists() or Choice == "3":
        if Choice == "1":
            print(i)
            shutil.move(i, Destination)
        elif Choice == "2":
            print(i)
            shutil.copy(i, Destination)
    else:
        print("The destination is not available; the operation will be aborted \nOr you chose to exit the execution")
        break

input("The process is complete. Press Enter to close.    ")