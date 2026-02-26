import pandas as pd
import pytest
from src.reader import load_contacts

def test_load_contacts_empty_file(tmp_path):
    """Verify the reader returns an empty list for a file with no data."""
    d = tmp_path / "empty.xlsx"
    df = pd.DataFrame(columns=['name', 'email', 'company'])
    df.to_excel(d, index=False)
    
    contacts = load_contacts(str(d))
    assert len(contacts) == 0

def test_load_contacts_missing_columns(tmp_path):
    """Ensure it handles files missing required columns."""
    d = tmp_path / "bad_cols.xlsx"
    df = pd.DataFrame({"name": ["Test"], "city": ["New York"]})
    df.to_excel(d, index=False)
    
    contacts = load_contacts(str(d))
    assert contacts == []