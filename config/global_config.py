from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
import os
from dotenv import load_dotenv
load_dotenv()

name_parameters = [['Дата', 'Курс доллара', "Курс евро"]]
engine = create_engine(f"postgresql://{os.getenv('USER_DB')}:{os.getenv('PASSWORD_USER')}@{os.getenv('API_DB')}/{os.getenv('NAME_DB')}", echo=True)
base = declarative_base()
