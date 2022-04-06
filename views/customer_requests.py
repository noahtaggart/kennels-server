CUSTOMERS = [
    {
        "id": 1,
        "first_name": "Mathias",
        "last_name": "Fey"
    }, {
        "id": 2,
        "first_name": "Cathee",
        "last_name": "Cock"
    }, {
        "id": 3,
        "first_name": "Matty",
        "last_name": "Coke"
    }, {
        "id": 4,
        "first_name": "Larissa",
        "last_name": "Joinsey"
    }, {
        "id": 5,
        "first_name": "Lilah",
        "last_name": "Mattheeuw"
    }
]

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    requested_customer = None
    
    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer
            
    return requested_customer
