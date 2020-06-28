from colorama import Fore

def run():
    print()
    print('***************************** WELCOME ***************************')
    print()

    show_commands()

    while True:
        action = get_action()
        
        switcher = {
            'e': enter_mood_ranking,
            'v': view_mood_rankings,
            'c': calculate_mood_swings,
            'x': exit_app,
            '?': show_commands,
            '': lambda: None,
        }
        
        func = switcher.get(action, unknown_command)
        func()
        # func()
        
        

        # with switch(action) as s:
        #     s.case('a', add_record)
        #     s.case('e', export_records)
        #     s.case('g', generate_labels)
        #     s.case('l', list_records)
        #     s.case('f', find_record)
        #     s.case(['x', 'bye', 'exit', 'exit()'], exit_app)
        #     s.case('?', show_commands)
        #     s.case('', lambda: None)
        #     s.default(unknown_command)

        # if action:
        #     print()

        # if s.result == 'change_mode':
        #     return

def show_commands():
    print('What action would you like to take:')
    print('[E]nter mood ranking for today')
    print('[V]iew previous mood rankings')
    print('[C]alculate current & upcoming mood swing')
    print('e[X]it app')
    print('[?] Help (this info)')
    print()

# Menu Commands #

def enter_mood_ranking():
    print(' ****************** NOT IMPLEMENTED ****************** ')
    return NotImplemented

def view_mood_rankings():
    print(' ****************** NOT IMPLEMENTED ****************** ')
    return NotImplemented

def calculate_mood_swings():
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
