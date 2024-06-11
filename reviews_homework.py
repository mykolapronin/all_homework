from pywebio.input import textarea, select, checkbox, radio, FLOAT, DATE, PASSWORD, DATETIME, input as input_pw, slider
from pywebio.output import put_success, put_error, put_warning, put_image, put_html
from pywebio.session import run_js
from pywebio import start_server

positive_emotions = ['Дуже сподобалось', 'У захваті', ]
negative_emotions = ['Негативні емоції', 'Не задоволений(-а)']
emotions = positive_emotions + negative_emotions

epic_genre = ['Фантастика', 'Бойовик']
regular_genre = ['Драма', 'Комедія']
genre_options = epic_genre + regular_genre

reviews_info = []


def main():
    put_html('<h1>Программа по збору відгуків по фільмах </h1>')
    name = input_pw("Введіть ваше ім'я", required=True)
    film_name = input_pw("Введіть назву фільму", required=True)
    film_genre = select("Виберіть жанр фільму", options=genre_options)
    short_review = textarea('Напишіть короткий відгук')
    film_rating = slider('Яка ваша оцінка до фільму', min_value=1, max_value=10)
    your_emotions = checkbox('Які були ваші емоції після перегляду', options=emotions)
    recomendation = radio('Чи рекомендуєте цей фільм іншим', options=['Так', 'Ні'])
    if film_rating == 10 or film_rating == 9 or film_rating == 8:
        put_success('Дякуємо за оцінку!')

    reviews_info.append([name, film_name, film_genre, short_review, film_rating, your_emotions, recomendation])
    run_js('setTimeout(function(){location.reload();}, 4000)')


if __name__ == '__main__':
    start_server(main, port=10000)
