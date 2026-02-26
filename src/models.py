from pydantic import BaseModel, EmailStr, field_validator

class Contact(BaseModel):
    name: str
    email: EmailStr
    
    @field_validator('name')
    @classmethod
    def normalize_name(cls, value: str) -> str:    
        if not value.strip():
            raise ValueError('Name field cannot be empty')
        return value.strip().title()
    
    @field_validator('email')
    @classmethod
    def lowercase_email(cls, value: str) -> str:
        return value.lower()