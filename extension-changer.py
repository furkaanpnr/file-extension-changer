from os import scandir,rename,chdir
from termcolor import colored
from time import sleep

try:
    PATH = chdir("") # * Change this to your path
    extensionToChange = "" # * Change this to your extension
    desiredExtension = ""  # * Change this to your desired extension
    with scandir(PATH) as entries:
        sleep(0.003)
        counter = 0
        print(colored("\nRenaming files...","grey"))
        for entry in entries:
            if entry.name.endswith(extensionToChange): #Check if the file ends with the extension to be changed
                counter += 1
                rename(entry.name, entry.name.replace(extensionToChange, desiredExtension))#Replace the extension
                sleep(0.02)
        print(colored(f"---> {counter} file extensions changed!", "green"))#Print the number of files changed

except KeyboardInterrupt:
    print(colored(f"\n---> Manually Stopped!", "blue"))#Print if the user stops the program manually
    print(colored(f"---> {counter} file extensions changed!", "green"))#Print the number of files changed
    exit(0)
    
except FileNotFoundError:
    print(colored(f"\n---> Path is not found!", "red"))#Print if the path is not found
    exit(0)


    

    