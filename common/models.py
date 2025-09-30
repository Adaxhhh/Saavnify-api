from pydantic import BaseModel
from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class ResponseModel(BaseModel, Generic[T]):
    success: bool
    data: T

class ErrorResponse(BaseModel):
    success: bool = False
    message: str
    error_code: Optional[int] = None
