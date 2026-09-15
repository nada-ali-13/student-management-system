
def validate_name(name):
    if not name.strip():
        raise ValueError("Name cannot be empty")

def validate_age(age):
    if age < 16:
        raise ValueError("Age is too low")

def validate_email(email):
    if "@" not in email:
        raise ValueError("Invalid email")

def validate_phone(phone):
    if not phone.strip():
        raise ValueError("Phone cannot be empty")