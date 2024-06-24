import requests

url = 'https://dummyjson.com/users?limit=300'

list_of_twenty_eight_years_old_users = []


def get_user_name_by_age(age: int = 28):
    response = requests.get(url=url)
    response_json = response.json()
    users = response_json['users']
    for user in users:
        if user['age'] == age:
            list_of_twenty_eight_years_old_users.append(user['firstName'], )
    return list_of_twenty_eight_years_old_users


start_function_get_username = get_user_name_by_age()
print(start_function_get_username)
