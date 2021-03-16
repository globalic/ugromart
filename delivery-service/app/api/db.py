import os

from sqlalchemy import (
    ARRAY,
    Column,
    create_engine,
    Date,
    DateTime,
    Decimal,
    Integer,
    MetaData,
    String,
    Table,
)

import timezone
from databases import Database

DATABASE_URI = os.getenv("DATABASE_URI")

engine = create_engine(DATABASE_URI)
metadata = MetaData()

deliveries = Table(
    "delivery",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("delivery_date", Date, nullable=False, index=True, default=timezone.now),
    Column("delivery_no", String(50), nullable=False),
    Column("amount", Decimal(10, 7), nullable=False),
    Column("order_id", Integer),
    Column("delivery_status_id", Integer),
    Column("payments_id", ARRAY(Integer)),
)

database = Database(DATABASE_URI)
