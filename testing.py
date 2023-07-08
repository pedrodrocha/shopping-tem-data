from models.Shopping import Shopping
from models.ShoppingPhone import ShoppingPhone  # ruff: noqa: F401
from shopping_data import Session

with Session() as session:
    shopping = Shopping(
        name = "Shopping Eldorado",
        site_url="https://www.shoppingeldorado.com.br/",
    )

    session.add(shopping)
    session.commit()

