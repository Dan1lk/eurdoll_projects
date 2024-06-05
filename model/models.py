import datetime
from config.global_config import base
from sqlalchemy.orm import Mapped, mapped_column

class UsdEur(base):
    __tablename__ = 'Курс_доллара_евро_за_период'
    id: Mapped[int] = mapped_column(nullable=False, unique=True, primary_key=True, autoincrement=True)
    date: Mapped[datetime.date]
    rate_usd: Mapped[float]
    rate_eur: Mapped[float]