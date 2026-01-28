import requests


response = requests.get(
    "https://www.cbr-xml-daily.ru/daily_json.js",
    timeout=5  # ждать ответа не более 5 секунд
    )
# Преобразуем ответ в .json формат.
data = response.json()

# Из данных находим по ключам словаря .json нужное значение с ключом
valute_dict = {
    "Доллар США": data["Valute"]["USD"]["Value"],
    "Евро": data["Valute"]["EUR"]["Value"],
    "Фунт стерлингов": data["Valute"]["GBP"]["Value"],
    "Дирхам ОАЭ": data["Valute"]["AED"]["Value"],
    "Юань": data["Valute"]["CNY"]["Value"]
}
name_of_data = list(valute_dict.keys())
valutes_of_data = list(valute_dict.values())


if __name__ == "__main__":
    print(data)
    print(f"Доллар США: {valute_dict['Доллар США']} руб.")
    print(f"Евро: {valute_dict['Евро']} руб.")
    print(f"Фунт стерлингов: {valute_dict['Фунт стерлингов']} руб.")
    print(f"Дирхам ОАЭ: {valute_dict['Дирхам ОАЭ']} руб.")
    print(f"Юань: {valute_dict['Юань']} руб.")
