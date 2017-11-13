from products import products

discount_list = [
    {
        "code": "APOM",
        "rules": [
            {
                "items": (products["oatmeal"]["code"], products["oatmeal"]["price"]),
                "comparator": ">=",
                "quantity": 1
            },
            {
                "items": (products["apples"]["code"], products["apples"]["price"]),
                "comparator": ">=",
                "quantity": 1
            }
        ],
        "credit": "-3.00",
        "apply_to": "AP1"
    },
    {
        "code": "APPL",
        "rules": [
            {
                "items": (products["apples"]["code"], products["apples"]["price"]),
                "comparator": ">=",
                "quantity": 3
            }
        ],
        "credit": "-1.50",
        "apply_to": "AP1",
        "special": "each"
    },
    {
        "code": "BOGO",
        "rules": [
            {
                "items": (products["coffee"]["code"], products["coffee"]["price"]),
                "comparator": ">=",
                "quantity": 2
            }
        ],
        "credit": "-11.23",
        "apply_to": "CF1"
    },
    {
        "code": "CHMK",
        "rules": [
            {
                "items": (products["chai"]["code"], products["chai"]["price"]),
                "comparator": ">=",
                "quantity": 1
            },
            {
                "items": (products["milk"]["code"], products["milk"]["price"]),
                "comparator": ">=",
                "quantity": 1
            }
        ],
        "limit": 1,
        "credit": "-4.75",
        "apply_to": "MK1"
    }
]
