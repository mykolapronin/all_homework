import requests

url = ("https://script.googleusercontent.com/macros/echo?user_content_key"
       "=xknNrg38aguF4ATdhlJHcKLgUJR8RkXsn9uiHrUlty5b8mxVPCbELf5TXSciUSISnnJtQ7G2XDzOd8jIHGT2rjoP"
       "-i6sm7CDm5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnMC9GLsfBIjbqTtNu98ExKJ_WnIY0RjG8TU35kib8"
       "-AbHZ9bCrwNBSrF410i0FPPpGxxi8CfG_fCUXnCOwKL8JxQkU1zsCysYdz9Jw9Md8uu&lib=M5x8Nf5L-74RVGWYLIk2Md7wiMsjcalLq")


def get_animals() -> list[dict]:
    response = requests.get(url=url)
    response_json = response.json()
    animals = response_json["animals"]
    print(animals)
    return animals


def get_total_caring_cost(animals):
    result_cost = 0
    for animal in animals:
        if animal["poison"]:
            total_caring_cost = animal["cost_of_caring"] * animal["number_of_animals"]
            result_cost += total_caring_cost
    return result_cost


def get_animal_data_from_africa(animals):
    animals_from_africa = []
    for animal in animals:
        if animal["origin_of_animal"] == "Африка":

            animals_from_africa.append(animal["animal"])
    return animals_from_africa


def main():
    animals = get_animals()
    total_caring_cost = get_total_caring_cost(animals)
    african_animals = get_animal_data_from_africa(animals)
    print(f'Стільки буде коштувати доглядати за отруйними тваринами: {total_caring_cost}')
    print(f'Ось які тварини були привезені з Африки : {african_animals}')


if __name__ == "__main__":
    main()

