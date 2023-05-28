import pytest


@pytest.fixture
def test_data():
    return [
        {
            "id": 373912477,
            "state": "CANCELED",
            "date": "2018-03-09T02:11:01.339352",
            "operationAmount": {
                "amount": "33249.01",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Visa Classic 7022985698476865",
            "to": "Счет 60979028617970883410"
        },
        {
            "id": 720751477,
            "date": "2018-11-08T08:21:45.902633",
            "operationAmount": {
                "amount": "16872.46",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75743795418434298755",
            "to": "Счет 80785963509390811744"
        },
        {
            "id": 949194534,
            "state": "EXECUTED",
            "date": "2019-08-15T01:48:10.042554",
            "operationAmount": {
                "amount": "31222.43",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 65298957349197687907",
            "to": "Счет 38784565940893479418"
        },
        {
            "id": 260972664,
            "state": "EXECUTED",
            "date": "2018-01-23T01:48:30.477053",
            "operationAmount": {
                "amount": "2974.30",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 3414396880443483",
            "to": "Visa Gold 2684274847577419"
        },
        {
            "id": 317987878,
            "state": "EXECUTED",
            "date": "2018-01-13T13:00:58.458625",
            "operationAmount": {
                "amount": "55985.82",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 8906171742833215",
            "to": "Visa Platinum 6086997013848217"
        },
        {
            "id": 207126257,
            "state": "EXECUTED",
            "date": "2017-07-15T11:47:40.496961",
            "operationAmount": {
                "amount": "92688.46",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 35737585785074382265"
        },
        {
            "id": 547682597,
            "state": "EXECUTED",
            "date": "2016-12-29T21:45:18.495053",
            "operationAmount": {
                "amount": "66263.93",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 77977573135347241529",
            "to": "Счет 33062909508148771891"
        }
    ]
