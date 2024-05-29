# Відпочинок з друзями
people = 4

ticket = 500 * people

taxi_to = 600
taxi_out = taxi_to * 1.2
taxi_trip = taxi_out + taxi_to

pizza = 250 * 2

pizza_discount = pizza * 0.85

air_hockey = 8 * 80

final_check = ticket + taxi_trip + pizza_discount + air_hockey
print(f'Весь чек буде: {final_check} гривень, Кожен з вас має заплатити: {final_check / 4}')
