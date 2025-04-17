from pydantic import BaseModel, Field


class FreeOffer(BaseModel):
    sku: str
    min_count: int
    free_sku: str = Field(default=None)
