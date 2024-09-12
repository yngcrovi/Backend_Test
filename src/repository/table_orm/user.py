from sqlalchemy.orm import Mapped, mapped_column
from .declarative_base.declarative_base import Base
import datetime

class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    hash_password: Mapped[bytes] = mapped_column(nullable=False)
    date_registration: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now)


    repr_cols_num = 3


