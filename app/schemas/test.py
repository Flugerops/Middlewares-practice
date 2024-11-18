from pydantic import BaseModel,Field


class TestScheme(BaseModel):
    name: str = Field(..., example="Nuclear bomb", description="Name of the item")
    description: str | None = Field(None, example="This is a test item", description="Description of the item")
    price: float = Field(..., gt=0, example=14.88, description="Item cost, must be above 0")

