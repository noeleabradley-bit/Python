import datetime
import re

def validate_date(date_text: str) -> str:
    """Ensures input conforms to YYYY-MM-DD format."""
    try:
        valid_date = datetime.datetime.strptime(date_text.strip(), "%Y-%m-%d").date()
        return str(valid_date)
    except ValueError:
        return None


def validate_phone(phone_text: str) -> str:
    """Strips formatting clutter and validates an international phone number sequence."""
    cleaned = re.sub(r"[\s\-\(\)]", "", phone_text.strip())
    pattern = r"^\+?[0-9]{7,15}$"
    return cleaned if re.match(pattern, cleaned) else None


def prompt_user(message: str, allow_empty: bool = False) -> str:
    """Helper to clean text prompts and enforce mandatory fields."""
    while True:
        value = input(message).strip()
        if not value and not allow_empty:
            print("Error: This field cannot be left blank.")
            continue
        return value if value else None