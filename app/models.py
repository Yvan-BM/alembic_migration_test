from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass 


class Item(Base):
    __tablename__ = 'items'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(server_default='0')
    quantity: Mapped[int] = mapped_column(server_default='0')
    group: Mapped[int] = mapped_column(nullable=True)
    designation: Mapped[str] = mapped_column(nullable=True)
    section: Mapped[str] = mapped_column(nullable=True)
    label: Mapped[str] = mapped_column(nullable=True)

class User(Base):
    __tablename__ = 'user'

    id : Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(nullable=True)