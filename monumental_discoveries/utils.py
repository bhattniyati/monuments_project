"""
Keep utils functions
"""

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

    for field_name, display_name in required_fields.items():
        if not request_data.get(field_name):
            error_list.append(f"{display_name} is required")

    if str(request_data["password"]).lower() != str(request_data["cpassword"]).lower():
        error_list.append("Password and confirm password are not the same")

    if error_list:
        return False, error_list
    return True, error_list
