from pydantic import BaseModel, Field


class FreeOffer(BaseModel):
    sku: str
    min_count: int = Field(default=1)
    free_sku: str = Field(default=None)
