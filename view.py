import menu
import add_employees as addem
import controller_module as controller


def button():
    menu.main_title()
    menu.main_menu()

    select_num = int(input('Выберите пункт меню: '))

    if select_num == 1:
        addem.add_employees()
    elif select_num == 2:
        controller.print_x()
