from models.Models import Shopping
from shopping_data import Session

with Session() as session:
    shopping = Shopping(
        name = "Shopping Eldorado",
        site_url="https://www.shoppingeldorado.com.br/",
    )

    session.add(shopping)
    session.commit()

