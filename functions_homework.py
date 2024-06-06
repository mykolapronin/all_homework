from pywebio.output import put_html


def greeting_user(user_name):
    welcome_string = put_html(f'<h1>Вітаємо тебе, шановний {user_name}</h1>')
    return str(welcome_string)


# nickname = greeting_user('kolya')
# print(nickname)


def counting_area_of_rectangle(first_diagonal, second_diagonal):
    result = first_diagonal * second_diagonal
    return result

# s = counting_area_of_rectangle(6, 4)
# print(s)
