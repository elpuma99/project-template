from colorama import Fore
import program_menu

def main():
    print_header()

    try:
        while True:
            program_menu.run()

    except KeyboardInterrupt:
        return
    
    
def print_header():
    
    print(Fore.WHITE + '****************  PROJECT TEMPLATE PROGRAM  ****************')
    print(Fore.WHITE + '****************************************************************')
    print()
    print("Welcome to the Project Template Program!")
    
if __name__ == "__main__":
    main()