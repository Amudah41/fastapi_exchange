from pydantic import BaseModel, Field


class CurrencyExchange(BaseModel):
    from_currency: str = Field(pattern=r"^[A-Za-z]{3}", default="GBP", max_length=3)
    to_currency: str = Field(pattern=r"^[A-Za-z]{3}", default="EUR", max_length=3)
    amount: float = 1


class CurrencyExchangeResponse(BaseModel):
    result: float


class ListOfCurrencies(BaseModel):
    currencies: dict[str, str]
