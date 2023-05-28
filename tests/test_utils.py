import pytest
from utils import get_data, get_filtered_data, get_last_values, get_formatted_data


def test_get_data():
    data = get_data()
    assert isinstance(data, list)


def test_get_filtered_data(test_data):
    assert len(get_filtered_data(test_data)) == 5


def test_get_last_values(test_data):
    data = get_last_values(test_data, 3)
    assert [x['date'] for x in data] == ["2019-08-15T01:48:10.042554", "2018-11-08T08:21:45.902633", "2018-03-09T02:11:01.339352"]


def test_get_formatted_data(test_data):
    assert get_formatted_data(test_data[-3:]) == ['13.01.2018 Перевод с карты на карту\nVisa Classic 8906 17** **** 3215 -> Visa Platinum 6086 99** **** 8217\n55985.82 USD',
                                                  '15.07.2017 Открытие вклада\n  -> Счет **2265\n92688.46 руб.',
                                                  '29.12.2016 Перевод организации\nСчет **1529 -> Счет **1891\n66263.93 руб.']
