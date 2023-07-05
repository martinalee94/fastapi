from sqlalchemy import Column, Integer, MetaData, String, Table, func
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import mapper
import secrets
import string

from app.domain import models

metadata = MetaData()


def sn_alphanum(length: int = 10) -> str:
    return "".join(
        secrets.choice(string.ascii_uppercase + string.digits[1:])
        for i in range(length)
    )


def generate_product_serial_number():
    return "PDT-" + sn_alphanum()


products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column(
        "create_dt",
        postgresql.TIMESTAMP(timezone=True),
        default=func.now(),
        server_default=func.now(),
    ),
    Column(
        "update_dt",
        postgresql.TIMESTAMP(timezone=True),
        default=func.now(),
        server_default=func.now(),
        onupdate=func.current_timestamp(),
    ),
    Column(
        "product_serial_number",
        String(14),
        unique=True,
        index=True,
        default=generate_product_serial_number,
    ),
    Column("title", String),
    Column("quantity", Integer),
    Column("price", Integer),
)


def start_mappers():
    products_mapper = mapper(models.Product, products)
