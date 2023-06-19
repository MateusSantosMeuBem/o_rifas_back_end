"""Services related to Google Sheets."""

from services.credentials import (
    CONFIG
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

def get_info_as_list() -> dict:
    """
    Convert dataframe into a list of dict:

    Return (list):
        List of dicts.
    """

    return get_table_info().to_dict(orient='records')
