import pytest
from pydantic import ValidationError
from src.models import Contact

def test_contact_normalization():
    """Verify that name, email, and company are correctly formatted."""
    data = {"name": "  jane smith  ", "email": "JANE@Example.com", "company": "  OpenAI  "}
    contact = Contact(**data)
    assert contact.name == "Jane Smith"
    assert contact.email == "jane@example.com"
    assert contact.company == "OpenAI"

def test_contact_invalid_email():
    """Ensure invalid emails raise a ValidationError."""
    with pytest.raises(ValidationError):
        Contact(name="Jane", email="not-an-email", company="Tech")