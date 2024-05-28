MSG_INPUT_WHICH_DISH = "Яка страва вам подобається? "
MSG_INPUT_RECIPE = "Введіть рецепт обраної страви: "

which_dish = input(MSG_INPUT_WHICH_DISH).title().strip()

recipe = input(MSG_INPUT_RECIPE).title()

header = 50 * '~'
footer = 50 * '~'
print(header)
print(f'страва: {which_dish} \n рецепт: {recipe}')
print(f"к-сть слів 'мясо': {recipe.count('Мясо')} ")
print(footer)
