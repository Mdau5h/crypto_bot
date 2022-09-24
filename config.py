import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    TOKEN: str = os.getenv('TOKEN')


config = Config()
