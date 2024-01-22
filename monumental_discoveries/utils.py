"""
Keep utils functions
"""
from .models import User

import re

def validate_data(request_data: dict):
    """
    This function is used to validate registration data
    """
    error_list = []
    required_fields = {
        "fname": "First name",
        "lname": "Last name",
        "uname": "Username",
        "email": "Email",
        "phoneno": "Phone number",
        "gender": "Gender",
        "password": "Password",
        "cpassword": "Confirm password",
    }

    # Email validation regex pattern
    email_pattern = re.compile(r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$')

    for field_name, display_name in required_fields.items():
        value = request_data.get(field_name, "").strip()

        if not value:
            error_list.append(f"{display_name} is required")
        elif field_name == "email" and not email_pattern.match(value):
            error_list.append("Invalid email format")
        elif field_name == "password" and len(value) < 8:
            error_list.append("Password must be at least 8 characters long")

    if str(request_data["password"]).lower() != str(request_data["cpassword"]).lower():
        error_list.append("Password and confirm password are not the same")

    if len(request_data["phoneno"]) != 10:
        error_list.append("Invalid phone number. Phone number must be 10 digits long")

    if request_data.get("email"):
        email_data = User.objects.filter(email=request_data["email"]).first()
        if email_data:
            error_list.append("This email is already taken, please try with a different email id")

    if request_data.get("uname"):
        username_data = User.objects.filter(username=request_data["uname"]).first()
        if username_data:
            error_list.append("This username is already taken, please try with a different username")

    if error_list:
        return False, error_list

    return True, error_list
