from sqlalchemy.orm import Mapped, mapped_column
from src.repository.table_orm.declarative_base.declarative_base import Base

class Product(Base): 
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name_product: Mapped[str] = mapped_column(unique=True)
    type_product: Mapped[str]
    calories: Mapped[int]
    protein: Mapped[float] 
    fat: Mapped[float]
    carbohydrates: Mapped[float]
    price: Mapped[int]

    repr_cols_num = 3