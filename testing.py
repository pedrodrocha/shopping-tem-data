from datetime import time

from models.Shopping import Shopping
from models.ShoppingAddress import ShoppingAddress  # ruff: noqa: F401
from models.ShoppingOpeningHour import ShoppingOpeningHour, WeekDays  # ruff: noqa: F401
from models.ShoppingPhone import ShoppingPhone  # ruff: noqa: F401
from shopping_data import Session

with Session() as session:
    shopping = Shopping(
        name = "Shopping Eldorado",
        site_url="https://www.shoppingeldorado.com.br/",
    )

    phone = ShoppingPhone(
        phone= 123456,
    )
    shopping.shopping_phones.append(phone)

    address = ShoppingAddress(
        address_line_1="asd",
        address_line_2=None,
        state="SP",
        city="SP",
        postal_code=1230,
    )

    shopping.shopping_address = address

    opening = ShoppingOpeningHour(
        week_day=WeekDays.sunday,
        opening_hour=time(4,50,10),
        closing_hour=time(10,50,10),
    )
    shopping.shopping_opening_hours.append(opening)

    session.add(shopping)

    session.commit()

