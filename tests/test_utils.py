
from utils import open_operations_json, numbers, sort_dict_by_date, last_five_count, code_text

def test_open_operations_json(test_url):
    assert open_operations_json(test_url)
    assert open_operations_json("README.md")
    assert open_operations_json("py.txt")


def test_numbers(test_number):
    assert numbers(test_number)

def test_sort_dict_by_date(test_by_date):
    assert sort_dict_by_date(test_by_date)


def test_last_five_count(test_by_date):
    assert last_five_count(test_by_date, 5)

def test_code_text():
    assert code_text('Счет 41421565395219882431')
    assert code_text('Maestro 1596837868705199')
    assert code_text('Visa Gold 9447344650495960')
