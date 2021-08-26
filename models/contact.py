from typing import Optional
from pydantic import BaseModel

class Contact(BaseModel):
    id : Optional[str]
    name: str
    lastname: str
    address: str
    email: str
    birthday: str

