from pywebio.output import put_html


def greeting_user_with_header_h1(user_name):
    welcome_string = put_html(f'<h1>Вітаємо тебе, шановний {user_name}</h1>')
    return str(welcome_string)


# nickname = greeting_user('kolya')
# print(nickname)


def calculating_area_of_rectangle(length, width):
    result = length * width
    return result

# s = calculating_area_of_rectangle(6, 4)
# print(s)
