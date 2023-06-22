"""Services related to Google Sheets."""

from flask import (
    abort
)

import pandas as pd
from pandas.core.frame import (
    DataFrame
)

from services.credentials import (
    CONFIG
)

def get_table_info() -> DataFrame:
    """
    Get table info from Google Sheets.

    Return (DataFrame):
        Values from Google Sheets table.
    """

    SHEET_ID = CONFIG.sheet_id
    SHEET_NAME = CONFIG.sheet_name
    url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'

    dataframe: DataFrame = pd.read_csv(url)
    dataframe = dataframe.rename(columns={'Número': 'number', 'Vendido': 'sold'})

    return dataframe


def get_info_as_list() -> list:
    """
    Convert dataframe into a list of dict:

    Return (list):
        List of dicts.
    """

    return get_table_info().to_dict(orient='records')


def get_seller(name: str) -> dict:
    """
    Get seller info from Google Sheets.

    Args:
        name (str): Name of the person.

    Return (SellerSchema):
        Seller info.
    """
    seller = {}
    seller['seller_name'] = name
    seller['numbers'] = get_personal_numbers(name)
    seller['pix'] = CONFIG.sellers.get(name).get('pix')
    seller['sold_numbers'] = 0
    seller['avaiable_numbers'] = 0

    for number in seller.get('numbers'):
        if number.get('sold') == 'SIM':
            seller['sold_numbers'] += 1
        else:
            seller['avaiable_numbers'] += 1

    return seller


def get_personal_numbers(name: str) -> list[int]:
    """
    Get personal numbers from Google Sheets.

    Args:
        name (str): Name of the person.

    Return (list):
        List of dicts.
    """

    try:
        seller = CONFIG.sellers.get(name)
        print(f'seller: {name}')

        numbers = [
            number
            for number in get_info_as_list()
            if (
                int(number.get('number')) >= seller.get('first_number') and
                int(number.get('number')) <= seller.get('last_number')
            )
        ]

        return numbers
    except KeyError:
        abort(404, f'Name {name} not found.')
    except Exception as error:
        abort(500, error)


def get_personal_message(name: str) -> str:
    """
    Get personal message from Google Sheets.

    Args:
        name (str): Name of the person.

    Return (str):
        Personal message.
    """

    personal_numbers = [
        number
        for number in get_personal_numbers(name)
        if number.get('sold') == 'NÃO'
    ]
    print(f'personal_numbers: {personal_numbers}')
    message = [f'Olá! Eu tenho os seguintes números disponíveis pra rifa:']
    message.append(
        ' | '.join(
            [   str(number.get('number'))
                for number in personal_numbers
            ]
        )
    )
    seller = CONFIG.sellers.get(name)
    message.append(f'<br>Chave PIX: {seller.get("pix")}')

    return '<br>'.join(message)

