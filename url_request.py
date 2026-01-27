import requests


response = requests.get(
    "https://www.cbr-xml-daily.ru/daily_json.js",
    timeout=5  # ждать ответа не более 5 секунд
    )
# Преобразуем ответ в .json формат.
data = response.json()
# Из данных находим по ключам словаря .json нужное значение
usd_data = data["Valute"]["USD"]["Value"]
eur_data = data["Valute"]["EUR"]["Value"]
gbp_data = data["Valute"]["GBP"]["Value"]
cny_data = data["Valute"]["CNY"]["Value"]
aed_data = data["Valute"]["AED"]["Value"]


if __name__ == "__main__":
    print(data)
    print(f"Дирхам ОАЭ: {aed_data} руб.")
    print(f"Юань: {cny_data} руб.")
    print(f"Фунт стерлингов: {gbp_data} руб.")
    print(f"Евро: {eur_data} руб.")
    print(f"Доллар США: {usd_data} руб.")
