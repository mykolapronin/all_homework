from pywebio.input import input as input_pw
from pywebio.input import NUMBER, FLOAT, DATE, TEXT
from pywebio.output import put_text, put_html, put_image
from pywebio import start_server
from pywebio.session import run_js

MSG_WELCOME = 'Вітаємо на супер-квізі!'
MSG_THANKS = "Дякуємо за участь!"


def getting_user_name():
    user_name = input_pw("Будь ласка введіть ваше ім'я")
    return user_name


def get_formatted_html_h2(message: str) -> str:
    result_h2 = f'<h2>{message}</h2> '
    return result_h2


def main():
    user_name = getting_user_name()
    total_score = 0
    question1 = input_pw('У якому році відбулося Водохреща Русі?', type=NUMBER)
    if question1 == 988:
        total_score += 1
    question2 = input_pw('Хто написав роман "Війна та мир"?', type=TEXT)
    if question2 == 'Лев Толстой':
        total_score += 1
    question3 = input_pw('Який елемент позначається символом "O" у періодичній таблиці?', type=TEXT)
    if question3 == 'Кисень':
        total_score += 1
    question4 = input_pw('Яка планета найбільша у Сонячній системі?', type=TEXT)
    if question4 == 'Юпітер':
        total_score += 1
    question5 = input_pw('Яке місто є столицею Австралії?', type=TEXT)
    if question5 == 'Канберра':
        total_score += 1

    put_html(f'{user_name}, Ви набрали {total_score} Балів')
    if total_score == 5:
        img = open('five_stars.jpeg', 'rb').read()
        put_image(img, width='20000px')
    put_html(get_formatted_html_h2(MSG_THANKS))

    run_js('setTimeout(function(){location.reload();}, 10000)')

if __name__ == '__main__':
    start_server(main, port=10000)

