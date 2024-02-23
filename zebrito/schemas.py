from typing import Literal
from pydantic import BaseModel, ConfigDict, Field, field_validator

class Transaction(BaseModel):
    total: int = Field(alias="valor")
    nature: Literal['c', 'd'] = Field(alias="tipo")
    description: str = Field(alias="descricao")

    @field_validator("total")
    @classmethod
    def validate_total(cls, value: int):
        if value <= 0:
            raise ValueError("Transaction should have a value greater than 0 (Zero)")
        return value

    @field_validator("description")
    @classmethod
    def validate_description(cls, value:str):
        if (1 <= len(value) <= 10):
            return value
        raise ValueError("A description should have between 1 and 10 characters")