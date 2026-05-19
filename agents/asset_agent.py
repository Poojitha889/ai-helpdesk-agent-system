assets = {
    "EMP001": {
        "employee": "John",
        "device": "Dell Laptop",
        "serial_number": "DL12345",
        "status": "Active"
    },

    "EMP002": {
        "employee": "Smith",
        "device": "MacBook Pro",
        "serial_number": "MB56789",
        "status": "Under Repair"
    },

    "EMP003": {
        "employee": "David",
        "device": "HP Laptop",
        "serial_number": "HP98765",
        "status": "Active"
    }
}


def get_asset_details(employee_id):

    employee_id = employee_id.upper()

    if employee_id in assets:
        return assets[employee_id]

    return {
        "message": "No asset found"
    }