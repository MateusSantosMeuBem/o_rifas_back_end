"""Services related to Google Sheets."""

from services.credentials import (
    CONFIG
)
from flask import (
    abort
)

import pandas as pd
from pandas.core.frame import (
    DataFrame
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


def get_personal_numbers(name: str) -> list:
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
                int(number.get('number')) <= seller.get('last_number') and
                number.get('sold') == 'NÃO'
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

    personal_numbers = get_personal_numbers(name)
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

