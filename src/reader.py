import pandas as pd
from typing import List
from .models import Contact 

def load_contacts(file_path: str) -> List[Contact]:
    try:
        # Load Excel file
        df = pd.read_excel(file_path)
        
        # Normalize column names
        df.columns = [str(c).strip().lower() for c in df.columns]
        
        # Check if required columns exist
        required_cols = {'name', 'email'}
        if not required_cols.issubset(df.columns):
            missing = required_cols - set(df.columns)
            print(f"Error: Missing required columns in Excel: {missing}")
            return []

        valid_contacts = []
        
        # Iterate and Validate
        for index, row in df.iterrows():
            try:
                # We extract values and pass them to our model
                contact = Contact(
                    name=str(row['name']),
                    email=str(row['email'])
                )
                valid_contacts.append(contact)
            except Exception as e:
                # If a row has validation error, keep going
                print(f"Row {index + 2} skipped: {e}")

        print(f"Total contacts successfully loaded: {len(valid_contacts)}")
        return valid_contacts

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except Exception as e:
        print(f"Unexpected error reading Excel: {e}")
        return []