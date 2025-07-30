from typing import Optional
from sqlmodel import SQLModel, Field
from sqlalchemy import Column, Numeric, Date
from decimal import Decimal
from datetime import date


class Orders(SQLModel, table=True):
    __tablename__ = "orders"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    customer_id: int = Field(foreign_key="customers.id")
    order_date: date = Field(sa_column=Column(Date))
    total_amount: Decimal = Field(sa_column=Column(Numeric(10, 2)))