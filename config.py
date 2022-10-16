import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    TOKEN: str = os.getenv('TOKEN')
    ADMIN_ID: int = int(os.getenv('ADMIN_ID'))


config = Config()
