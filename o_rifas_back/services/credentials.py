from dotenv import load_dotenv
import json
import os

from services.utils.path import (
    ROOT_PATH
)

class Config():
    """Google Sheets credentials."""

    def __init__(self) -> None:
        load_dotenv()

        self.sheet_id: str = os.getenv('SHEET_ID')
        self.sheet_name: str = os.getenv('SHEET_NAME')

        seler_path = os.path.join(ROOT_PATH, 'src', 'sellers.json')
        with open(seler_path, 'r') as json_file:
            self.sellers = json.load(json_file)

CONFIG = Config()