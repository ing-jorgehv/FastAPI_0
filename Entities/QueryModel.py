from pydantic import BaseModel

class QueryModel(BaseModel):
    param1: str = None
    param2: int = None
    param3: float = None
