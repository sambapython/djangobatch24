from django.core.exceptions import ValidationError

def validate_name(value):
    if not value.isalnum():
        raise ValidationError("Name expecting only numbers and alphabets")
    return value