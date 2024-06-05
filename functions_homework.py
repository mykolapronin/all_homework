from pywebio.output import put_html


def welcome_user(user_name):
    welcome_string = put_html(f'<h1>Вітаємо тебе, шановний {user_name}</h1>')
    return str(welcome_string)


# nickname = welcome_user('kolya')
# print(nickname)


def area_of_rectangle(multiplier, multiplied):
    result = multiplier * multiplied
    return result

# s = area_of_rectangle(6, 4)
# print(s)
