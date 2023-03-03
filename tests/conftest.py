import pytest

@pytest.fixture
def test_url():
    return "operations.json"

@pytest.fixture
def test_number():
    return [
      {
        "id": 285353808,
        "state": "EXECUTED",
        "date": "2018-08-06T16:22:54.643491",
        "operationAmount": {
          "amount": "82946.19",
          "currency": {
            "name": "руб.",
            "code": "RUB"
          }
        },
        "description": "Открытие вклада",
        "to": "Счет 12189246980267075758"
      },
      {
      },
      {
        "id": 416017997,
        "state": "EXECUTED",
        "date": "2019-05-07T01:32:37.142797",
        "operationAmount": {
          "amount": "29033.65",
          "currency": {
            "name": "USD",
            "code": "USD"
          }
        },
        "description": "Перевод с карты на карту",
        "from": "МИР 4878656375033856",
        "to": "Maestro 6890749237669619"
      },
      {
        "id": 556488059,
        "state": "CANCELED",
        "date": "2019-05-17T01:50:00.166954",
        "operationAmount": {
          "amount": "74604.56",
          "currency": {
            "name": "USD",
            "code": "USD"
          }
        }
      }
    ]

@pytest.fixture
def test_by_date():
    return [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
  {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  },
  {
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
  },
  {
    "id": 142264268,
    "state": "EXECUTED",
    "date": "2019-04-04T23:20:05.206878",
    "operationAmount": {
      "amount": "79114.93",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 19708645243227258542",
    "to": "Счет 75651667383060284188"
  }]

