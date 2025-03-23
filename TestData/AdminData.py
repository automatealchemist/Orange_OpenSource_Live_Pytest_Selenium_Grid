from TestData.EmployeeManagementData import EmployeeManagementData

class AdminData:
    # Fetch name_data once
    name_data = EmployeeManagementData.name_data

    # Extract first, middle, and last name safely
    first_name = name_data.get("first_name", "")
    middle_name = name_data.get("middle_name", "")
    last_name = name_data.get("last_name", "")

    # Ensure spaces while constructing the full name
    full_name = f"{first_name} {middle_name} {last_name}".strip()

    test_admin_data = [
        {
            "name": full_name,  # Use the corrected full_name
            "password": "Password@123",
            "confirmpassword": "Password@123"
        }
    ]
