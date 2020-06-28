from colorama import Fore

def run():
    print()
    print('***************************** WELCOME ***************************')
    print()

    show_commands()

    while True:
        action = get_action()
        
        switcher = {
            'f': first_menu_option,
            's': second_menu_option,
            't': third_menu_option,
            'x': exit_app,
            '?': show_commands,
            '': lambda: None,
        }
        
        func = switcher.get(action, unknown_command)
        func()

def show_commands():
    print('What action would you like to take:')
    print('[F]irst menu option')
    print('[S]econd menu option')
    print('[T]hird menu option')
    print('e[X]it app')
    print('[?] Help (this info)')
    print()

# Menu Commands #

def first_menu_option():
    print(' ****************** NOT IMPLEMENTED ****************** ')
    return NotImplemented

def second_menu_option():
    print(' ****************** NOT IMPLEMENTED ****************** ')
    return NotImplemented

def third_menu_option():
    print(' ****************** NOT IMPLEMENTED ****************** ')
    return NotImplemented


def exit_app():
    print()
    print('bye')
    raise KeyboardInterrupt()


def get_action():
    text = '> '
    # if state.active_account:
    #     text = f'{state.active_account.name}> '

    action = input(Fore.YELLOW + text + Fore.WHITE)
    return action.strip().lower()


def unknown_command():
    print("Sorry we didn't understand that command.")


def success_msg(text):
    print(Fore.LIGHTGREEN_EX + text + Fore.WHITE)


def error_msg(text):
    print(Fore.LIGHTRED_EX + text + Fore.WHITE)
