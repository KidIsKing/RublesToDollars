import requests


response = requests.get(
    "https://www.cbr-xml-daily.ru/daily_json.js",
    timeout=5  # ждать ответа не более 5 секунд
    )
# Преобразуем ответ в .json формат.
data = response.json()

# Из данных находим по ключам словаря .json нужное значение с ключом
valute_data = {
    "Доллар США": data["Valute"]["USD"]["Value"],
    "Евро": data["Valute"]["EUR"]["Value"],
    "Фунт стерлингов": data["Valute"]["GBP"]["Value"],
    "Дирхам ОАЭ": data["Valute"]["AED"]["Value"],
    "Юань": data["Valute"]["CNY"]["Value"]
}


if __name__ == "__main__":
    print(data)
    print(f"Доллар США: {valute_data["Доллар США"]} руб.")
    print(f"Евро: {valute_data["Евро"]} руб.")
    print(f"Фунт стерлингов: {valute_data["Фунт стерлингов"]} руб.")
    print(f"Дирхам ОАЭ: {valute_data["Дирхам ОАЭ"]} руб.")
    print(f"Юань: {valute_data["Юань"]} руб.")
