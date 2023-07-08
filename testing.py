from models.Shopping import Shopping
from models.ShoppingPhone import ShoppingPhone  # ruff: noqa: F401
from models.ShoppingAddress import ShoppingAddress  # ruff: noqa: F401
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
        postal_code=1230
    )

    shopping.shopping_address = address


    session.add(shopping)

    session.commit()

