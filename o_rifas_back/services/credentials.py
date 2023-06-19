from dotenv import load_dotenv
import os


class Config():
    """Google Sheets credentials."""

    def __init__(self) -> None:
        load_dotenv()

        self.sheet_id: str = os.getenv('SHEET_ID')
        self.sheet_name: str = os.getenv('SHEET_NAME')

CONFIG = Config()