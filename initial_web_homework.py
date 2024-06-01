from pywebio.input import input as input_pw

from pywebio.output import put_text, put_html, put_image

# header
put_html('<h1> Вітаємо вас із закінченням навчального року і з наступанням літа</h1>')

# input section

verse = """Вітер в полі розхитав
Голубий дзвіночок –
Забринів, затрепетав
Ніжний голосочок.

Цей чудовий літній день
Барвами чарує
І мелодії пісень
Щедро всім дарує.
 💙"""

put_text(verse)

plans_for_summer = input_pw('Розповідіть, будь ласка про свої плани на літо')
user_name = input_pw("Введіть ваше ім'я")

put_html(f'<h3>{plans_for_summer}</h3> <h5>{user_name}</h5>')
put_text(f"У ваших планах {len(plans_for_summer)} символів.")

img = open('sun.png', 'rb').read()
put_image(img, width='1500px')

