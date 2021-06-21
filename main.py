# Модуль автоматизации работы в Мвидео
# Python 3.9
__author__ = 'Vyacheslav Mitin <vyacheslav.mitin@gmail.com>'
__version__ = '1 - разработка'

import time
import pyautogui
# импорт селениума и сей его хуйня
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


# Функции
def print_log(text, line_before=False, line_after=False):
    """Функция формирования читабельной записи текущего действия.
    Параметры line_before=False, line_after=False для необходимости новых линий ДО и ПОСЛЕ вывода."""

    def time_log():
        """Функция формирования читабельной записи текущего времени (без даты)."""
        log_time = time.strftime("%H:%M:%S")  # формат '10:10:10'
        return log_time

    if line_before:  # линия ДО вывода сообщения
        print("")  # пустая строка

    print(f" {time_log()} | {text}")  # формат ' 13:05:02 | Текст'

    if line_after:  # линия ПОСЛЕ вывода сообщения
        print("")  # пустая строка


def start_dns(login_, password_):
    print_log('Запуск браузера с сайтом ДНС')
    browser = Firefox()
    browser.get('https://www.dns-shop.ru/')

    print_log("Логин")
    browser.find_element_by_class_name('header__login_button').click()
    time.sleep(3)
    pyautogui.click(x=745, y=538)
    time.sleep(3)
    pyautogui.press('tab', presses=2)
    time.sleep(1)
    pyautogui.write(login_, interval=1.5)  # логин
    pyautogui.press('tab')
    pyautogui.write(password_, interval=1.5)  # пароль
    time.sleep(1)
    pyautogui.press('enter')


    # browser.find_element_by_name('LOGIN').clear()
    # browser.find_element_by_name('LOGIN').send_keys(name_)
    # browser.find_element_by_name('pass').clear()
    # browser.find_element_by_name('pass').send_keys(password_)
    # browser.find_element_by_class_name('logo__form__button').click()
    #
    # if browser.current_url == 'http://10.0.1.78/DELO/main.aspx':
    #     pass
    # else:
    #     browser.find_element_by_name('btnTerminate').click()
    # browser.get('http://10.0.1.78/DELO/Pages/Cabinet/Folder.aspx?cabinet_id=54193&folder_id=1')


# Запуск модуля
if __name__ == '__main__':
    print(f"МОДУЛЬ РАБОТЫ БОТА\n{__author__}\nВерсия {__version__}\n")
    MODE = input('Введите режим, 1 - ДНС, 2 - Мвидео, 3 - Эльдорадо: ')

    if MODE == '1':
        start_dns(login_='drumgun666@gmail.com', password_='Qwerty123456')

    print_log('Окончание работы модуля', line_before=True)
