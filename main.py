from tkinter import Tk, ttk, PhotoImage
from datetime import datetime
from url_request import name_of_data, valutes_of_data
from read_statistics import old_valutes_of_data, info_is_ready


def save_change_prices():
    """Внесение информации об изменениях цен на валюты в txt файл."""
    info_list = []
    if info_is_ready:
        for i in range(len(valutes_of_data)):
            if old_valutes_of_data[i] != valutes_of_data[i]:
                price_delta = old_valutes_of_data[i] - valutes_of_data[i]
                if price_delta < 0:
                    info = "дороже"
                else:
                    info = "дешевле"
                info_list.append(
                    f"\"{name_of_data[i]}\" изменил цену c "
                    f"{old_valutes_of_data[i]} руб. на {valutes_of_data[i]} "
                    f"руб. Стало {info} на: {abs(price_delta):.3f} руб."
                )
            else:
                info_list.append(
                    f"Изменений цены для \"{name_of_data[i]}\" нет."
                    )
    else:
        for i in range(len(valutes_of_data)):
            info_list.append(
                f"Недостаточно информации для анализа \"{name_of_data[i]}\"."
                )
    return info_list


def save_info_prices(info_list):
    """Внесение информации о курсах валют в txt файл."""
    now = datetime.strftime(datetime.now(), "%H:%M:%S %d.%m.%Y")

    with open("statistics.txt", "a", encoding="utf-8") as file:
        file.write(f"============= Дата: {now}. =============\n")
        for i in range(len(valutes_of_data)):
            file.write(f"{valutes_of_data[i]} руб. - {name_of_data[i]}.\n")
        file.write("============== Информация об изменениях ==============\n")
        for info in info_list:
            file.write(
                f"{info}\n"
            )
        file.write(
                "============ Информация от Центробанка РФ ============\n\n\n"
            )


def visual():
    """Создание программы с курсами валют для визуала."""
    window = Tk()
    window.title("RublesToDollars")
    # window.geometry("500x500")

    icon = PhotoImage(file="img/yana_logo_1.png")
    window.iconphoto(True, icon)

    frm = ttk.Frame(window, padding=40)
    frm.grid()

    # Вывод текста с курсами валют в центре окна приложения.
    for i in range(len(valutes_of_data)):
        ttk.Label(
            frm,
            text=f"{name_of_data[i]}: {valutes_of_data[i]} руб."
        ).grid(column=0, row=i)

    ttk.Label(
        frm,
        text="Информация с сайта Центробанка РФ."
        ).grid(column=0, row=6)

    window.mainloop()


info_list = save_change_prices()
save_change_prices()
save_info_prices(info_list)
visual()
