EMPLOYEES = [
    {
        "id": 1,
        "first_name": "Berk",
        "last_name": "Waumsley"
    },
    {
        "id": 2,
        "first_name": "Ardyce",
        "last_name": "Selby"
    },
    {
        "id": 3,
        "first_name": "Harlene",
        "last_name": "Crackett"
    },
    {
        "id": 4,
        "first_name": "Martie",
        "last_name": "Pietzner"
    },
    {
        "id": 5,
        "first_name": "Frederic",
        "last_name": "Chorley"
    }
]


def get_all_employees():
    return EMPLOYEES


def get_single_employee(id):
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
