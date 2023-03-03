import datetime
import json
from datetime import datetime as dt


def open_operations_json(my_json):
    """
    С помощью функции считываем json файл
    """
    try:
        with open(my_json, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
                return data, "Данные получены успешно"
            except json.decoder.JSONDecodeError:
                return None, "ERROR: Это не json файл"
    except FileNotFoundError:
        return None, "ERROR: Файл отсутствует в данной директории"


def numbers(new_json):
    """
    С помощью функции получаем новый словарь, отсортированный по выполненным операциям
    """
    new_list = []
    for i in new_json:
        if "state" not in i:
            continue
        if i["state"] == 'EXECUTED':
            new_list.append(i)
    return new_list


def sort_dict_by_date(dict_list)->list:
    """
    Функция  сортирует список словарей по ключу date
    :param dict_list: исходный список словарей
    :return: отсортированный список словарей
    """
    dict_list_sorted = sorted(dict_list, key=lambda x: x['date'], reverse=True)
    return dict_list_sorted

def last_five_count(list_sort, number):
    """
    На старте функция принимает отсортированный список и число кол-во вывода операций
    Далее функция выводит информацию по последним переводам по дате.
    """
    text = ""
    for i in range(number):
        text += datetime.date.fromisoformat(list_sort[i]["date"][0:10]).strftime('%d-%m-%Y') + " "
        text += list_sort[i]["description"] + "\n"
        if "from" in list_sort[i]:
            text += code_text(list_sort[i]["from"]) + " -> "
        text += code_text(list_sort[i]["to"]) + "\n"
        text += list_sort[i]["operationAmount"]["amount"] + " " + list_sort[i]["operationAmount"]["currency"]["name"] + '\n\n'
    return text

def code_text(text):
    """
    Функия для шифровки номера карты или номера счета
    """
    new_list = text.split()
    if new_list[0] == "Счет":
        return new_list[0] + " **" + new_list[1][-4::]
    else:
        if len(new_list) >= 3:
            return new_list[0] + " " + new_list[1] + " " + new_list[-1][0:4] + " " + new_list[-1][4:6] + "** **** " + new_list[-1][12::]
        else:
            return new_list[0] + " " + new_list[-1][0:4] + " " + new_list[-1][4:6] + "** **** " + new_list[-1][12::]

